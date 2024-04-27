#!/bin/bash


sleep 10

uvicorn src.api.main:app --host gestion_horarios-back --reload