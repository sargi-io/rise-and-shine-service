# Rise and Shine
Rise and shine is simple backend service handling API connection to OpenAI and AWS Polly to create motivational speech in MP3
format. Currently only using GPT-3 model, which has limitation for creation personalized motivations based on bio. 
Plan is to upgrade once I will get access to ChatGPT model.

## Setup conda environment
```bash
conda create env create -f environment.yml
conda activate rise-and-shine
```

## Setup API keys
```bash
export OPENAI_API_KEY=**YOUR_OPENAI_API_KEY_HERE**
export AWS_ACCESS_KEY_ID_POLLY=**YOUR_ACCESS_KEY_ID_HERE**
export AWS_SECRET_ACCESS_KEY_POLLY=**YOUR_AWS_SECRET_ACCESS_KEY**
```

