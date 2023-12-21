#!/bin/bash
rm templates/cow*
flask --app main.py run --host=0.0.0.0
