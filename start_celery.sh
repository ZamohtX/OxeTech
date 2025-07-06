#!/bin/bash
export $(cat .env | xargs)
celery -A projeto worker --loglevel=info
