from openai import OpenAI

client = OpenAI()


def delete_fine_tuned_model(model_id):
    """Delete a fine-tuned model if the user is an owner of the organization."""
    try:
        client.models.delete(model_id)
        print(f"Model {model_id} successfully deleted.")
    except Exception as e:
        print(f"Failed to delete model {model_id}: {e}")


# Example usage
delete_fine_tuned_model("ft:gpt-4o-mini-2024-07-18:personal::ASd6rxOA")
