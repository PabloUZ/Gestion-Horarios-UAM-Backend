#!/bin/bash


sleep 10

uvicorn src.main:app --host gestion_horarios-back --reload