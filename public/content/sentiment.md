## The Challenge

Social media generates massive amounts of unstructured data that is often noisy and difficult to process efficiently. In Big Data analytics, the challenge lies in transforming raw, "dirty" JSON streams into structured insights while managing the infrastructure overhead of distributed computing.

This project addresses two specific hurdles:

1. **Data Engineering:** Processing a massive dataset of tweets (`JSON Lines`) to filter out bots, non-English content, and incomplete metadata to extract genuine sentiment[cite: 6, 20, 32].
2.  **Infrastructure Ops:** Deploying a legacy-compatible Hadoop 3.4.1 cluster on Docker, overcoming the **CentOS 7 End-of-Life (EOL)** repository failures that break standard builds.

## Methodology

The solution leverages a **MapReduce** architecture using Python's `mrjob` library, deployed on a multi-node Docker cluster.

1.  **Infrastructure & Automation:**

      * Patched the Hadoop Docker image to use **CentOS Vault** repositories, fixing EOL build errors.
      * Developed a dynamic Bash script (`setup_cluster.sh`) to auto-detect the Namenode container and inject data into HDFS, streamlining the deployment pipeline.

2.  **MapReduce Step 1: Ingestion & Filtering:**

      * **Mapper:** Implemented robust JSON parsing to discard tweets with null location/user data
      * **Logic:** Filtered exclusively for English tweets originating from the United States[cite: 33].
      * **Sentiment Scoring:** Applied the **AFINN-111** lexicon to tokenize text and calculate a sentiment score for every valid tweet

3.  **MapReduce Step 2: Statistical Aggregation:**

      * Designed a second pass to aggregate results globally.
      * Calculated the **happiest state** (Max Sentiment), generated a **Top 10 Hashtags** list (sorting by frequency), and computed **Device Usage** percentages

## Results

The pipeline successfully processed the dataset, turning unstructured noise into clear analytics.

  * **Sentiment Geography:** **Hawaii (HI)** was identified as the state with the highest positive sentiment (Score: 3.5), while states like Louisiana showed negative averages due to the specific weighting of the AFINN lexicon[cite: 55].
  * **Bot Detection:** The "Top Hashtags" analysis revealed a dominance of spam/bot tags (e.g., `#TeamFollowBack`, `#FF`), highlighting the importance of rigorous data cleaning in social media analysis[cite: 55].
  * **Device Battle:** The analysis showed a tight race in mobile adoption, with **iPhone (24.5%)** slightly leading over Web Clients and Android[cite: 55].

This project demonstrates the ability to maintain legacy Big Data infrastructure (Hadoop/Docker) while implementing complex ETL logic (MapReduce) to derive business intelligence from unstructured sources.