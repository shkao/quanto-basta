This transcript provides a detailed walkthrough of analyzing single-cell RNA and ATAC sequencing data, specifically for pediatric AML (Acute Myeloid Leukemia). Here's a structured summary of the key points, methodologies, and practical notes mentioned in the video:

### Introduction

- **Objective**: Provides an updated guide on single-cell RNA and ATAC analysis.
- **Data Set**: Longitudinal data set of pediatric AML including 28 patients with three time points each, and both RNA and ATAC from the same samples but different cells.

### Tools and Environment Setup

- **Tools Used**: Conda (for environment management), Python 3.9, Jupyter Notebook, ScanP, and Doublet Detection.
- **Libraries Imported**: OS (for file handling), ScanP (for data handling), Seaborn and Matplotlib (for plotting), NumPy, and Pandas (for data manipulation).

### Data Preparation and Pre-processing

- **Initial Steps**:
  - Download data and create a "data" directory.
  - Extract and organize downloaded files using terminal commands.
  - Fix file naming issues as ScanP expects certain standardized file names.

- **Required Pre-processing Adjustments**:
  - Replace non-standard file names using terminal commands.
  - Add a missing column to feature files to align with expected formats.

### Removing Ambient RNA

- **Tool Used**: CellBender by the Broad Institute.
  - Develop a separate Conda environment (Python 3.7) specifically for CellBender due to dependency conflicts.
  - Use CellBender to remove background RNA and determine actual cells, although CellBender’s cell determination might not be fully reliable.

### Further Pre-processing

- **File Conversion**: Convert matrix files into AND data (H5 AD) objects suitable for further analysis.
- **Quality Control (QC)**:
  - Annotate mitochondrial, ribosomal, and hemoglobin-related genes.
  - Analyze QC metrics like percentage of mitochondrial genes, number of genes, counts, etc.

- **Outlier Detection**:
  - Use Median Absolute Deviation (MAD) method to filter out low-quality cells.
  - Implement doublet detection method and iterate parameters to optimize results.

### QC Analysis

- **Plotting Distribution**: Generate ridge plots for visualizing distributions of percent mitochondrial content, number of genes, and counts to identify multicellular trends.
- **Data Cleaning**: Use doublet detection to refine data by removing artifacts (false multiplets).

### Summary and Recommendations

- **Validation**: Verify and interpret variations within the datasets to ensure no preprocessing errors.
- **Resources**: Recommended the Tice Lab’s single-cell best practices for deeper understanding.

### Future Steps

- **Cell Annotation**: Preparing to transition into more complex downstream analyses like cell annotation and integrated analysis.

This structured breakdown of the transcript provides a comprehensive overview of the methodologies, practical notes and tools used in the single-cell analysis process as described in the YouTube video.

Source URL: <https://www.youtube.com/watch?v=cmOlCTGX4Ik>
