# learn-actions

For vendor managed dependencies
1.  pipenv run pip freeze > requirements.txt
2.  pip install -r requirements.txt --target=vendor
3. rm -rf ./vendor/*dist-info
4. 