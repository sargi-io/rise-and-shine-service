# Readme
This project is simple backend service handling API connections to OpenAI and AWS Polly to create motivational speech in MP3
format. 

It sends prompt to GPT-3 model to generate text which is passed
to Azure Speech service.

## Setup conda environment
```bash
conda create env create -f environment.yml
conda activate rise-and-shine
```

## Setup API keys
```bash
export OPENAI_API_KEY=**YOUR_OPENAI_API_KEY_HERE**
export SPEECH_KEY=**YOUR_ACCESS_KEY_HERE**
export SPEECH_REGION=**YOUR_AWS_SECRET_ACCESS_KEY**
```

