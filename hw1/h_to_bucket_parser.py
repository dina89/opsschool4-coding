import json, yaml

with open('hw.json', encoding='utf8') as json_file:
    data = json.load(json_file)

    buckets = data['buckets']
    buckets.sort()

    results = dict()

    last_bucket = 0
    for bucket in buckets:
        bucket_name = str(last_bucket)+'-'+str(bucket) #+':'

        people_list = []
        for name,age in data['ppl_ages'].items():
            if last_bucket <= age < bucket:
                people_list.append(name)

        results[bucket_name] = people_list

        last_bucket = bucket

    max_age = last_bucket
    people_list = []
    for name, age in data['ppl_ages'].items():
        if last_bucket <= age:
            people_list.append(name)
            if age > max_age:
                max_age = age

    results[str(last_bucket)+'-'+str(max_age)] = people_list

    with open(r'result.yaml', 'w', encoding='utf8') as yaml_file:
        yaml.dump(results, yaml_file, allow_unicode=True)

    # with open('filename', 'w', encoding='utf8') as json_file:
    #     json.dump("ברי צקלה", json_file, ensure_ascii=False)