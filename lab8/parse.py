import json

with open('/Users/carriefeng/DS2022/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for repo in data[:5]:  # Extract only the first 5 repositories
        name = repo.get('name')
        html_url = repo.get('html_url')
        updated_at = repo.get('updated_at')
        visibility = repo.get('visibility')
        
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(csv_line)
        print(csv_line.strip())

