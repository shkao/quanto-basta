import os
import ollama
from loguru import logger
from pyzotero import zotero


def create_zotero_instance():
    library_id = os.getenv("ZOTERO_LIBRARY_ID")
    library_type = "user"
    api_key = os.getenv("ZOTERO_API_KEY")
    if not library_id or not api_key:
        logger.error("Zotero library ID or API key is not set.")
        raise EnvironmentError("Zotero library ID or API key is not set.")
    return zotero.Zotero(library_id, library_type, api_key)


def get_collection_by_name(zot, collection_name=".Inbox"):
    logger.info(f"Fetching collection '{collection_name}' from Zotero.")
    try:
        return next(
            (
                collection
                for collection in zot.everything(zot.collections())
                if collection["data"].get("name") == collection_name
            ),
            None,
        )
    except Exception as e:
        logger.error(f"Error fetching collections: {e}")
        return None


def retrieve_items(zot, collection_key, excluded_types=None, target_type=None):
    items = []
    try:
        items = zot.collection_items(collection_key)
        if excluded_types:
            items = [
                item
                for item in items
                if item["data"].get("itemType") not in excluded_types
            ]
        if target_type:
            items = [
                item for item in items if item["data"].get("itemType") == target_type
            ]
    except Exception as e:
        logger.error(f"Error fetching items from collection: {e}")
    return items


def get_inbox_items(zot):
    inbox_collection = get_collection_by_name(zot)
    if not inbox_collection:
        logger.warning("'.Inbox' collection not found.")
        return []
    return retrieve_items(
        zot, inbox_collection["key"], excluded_types=["attachment", "note"]
    )


def get_items_by_type(zot, item_type):
    valid_item_types = {
        "book",
        "bookSection",
        "conferencePaper",
        "dictionaryEntry",
        "encyclopediaArticle",
        "journalArticle",
        "manuscript",
        "note",
        "report",
        "thesis",
        "webpage",
    }

    if item_type not in valid_item_types:
        logger.error(
            f"Invalid item type '{item_type}'. Supported types are: {valid_item_types}"
        )
        return []

    inbox_collection = get_collection_by_name(zot)
    if not inbox_collection:
        logger.warning("'.Inbox' collection not found.")
        return []

    return retrieve_items(zot, inbox_collection["key"], target_type=item_type)


def summarize_abstract(abstract):
    prompt = (
        f"Summarize the following abstract in 3 sentences without any introductory phrases:\n\n"
        f"{abstract}"
    )
    try:
        response = ollama.chat(
            model="llama3.2", messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return ""

    return response.get("message", {}).get("content", "")


def append_summary_notes(zot, inbox_items):
    for item in inbox_items:
        children = zot.children(item["key"])
        if any(child["data"].get("itemType") == "note" for child in children):
            logger.debug(
                f"Skipping item {item['data'].get('title', 'Untitled')} as it already has a note."
            )
            continue

        abstract = item["data"].get("abstractNote", "")
        if abstract:
            logger.debug(
                f"Generating summary for item {item['data'].get('title', 'Untitled')}'."
            )
            summary = summarize_abstract(abstract)
            if summary:
                note = {
                    "itemType": "note",
                    "parentItem": item["key"],
                    "note": f"<p><b>Summary:</b> {summary}</p>",
                }
                try:
                    zot.create_items([note])
                    logger.info(
                        f"Added summary note for item '{item['data'].get('title', 'Untitled')}'."
                    )
                except Exception as e:
                    logger.error(f"Error adding summary note: {e}")


def delete_items_by_type(zot, item_type):
    logger.info(f"Removing items of type '{item_type}' from the '.Inbox' collection.")
    while True:
        inbox_items = get_items_by_type(zot, "note")
        logger.info(f"Retrieved {len(inbox_items)} items from the '.Inbox' collection.")
        items_to_remove = [
            item for item in inbox_items if item["data"].get("itemType") == item_type
        ]

        if not items_to_remove:
            break

        for item in items_to_remove:
            try:
                zot.delete_item(item)
                logger.info(
                    f"Removed item '{item['data'].get('title', 'Untitled')}' of type '{item_type}'."
                )
            except Exception as e:
                logger.error(
                    f"Error removing item '{item['data'].get('title', 'Untitled')}': {e}"
                )


def main():
    try:
        zot = create_zotero_instance()
        # delete_items_by_type(zot, "note")

        inbox_items = get_inbox_items(zot)
        append_summary_notes(zot, inbox_items)
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
