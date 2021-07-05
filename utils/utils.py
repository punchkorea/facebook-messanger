import csv

def read_profile_urls(filename):
    if not filename.endswith('.txt'):
        profile_urls = []
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                profile_url = line[4]
                if profile_url not in profile_urls:
                    profile_urls.append(profile_url)
        return profile_urls[1:]
    else:
        profile_urls = []
        with open(filename, 'r', encoding='utf-8') as text_file:
            for line in text_file:
                line = line.strip()
                profile_url = line
                if profile_url not in profile_urls:
                    profile_urls.append(profile_url)
        return profile_urls


def message_to_send():
    with open('message.txt', 'r', encoding='utf-8') as text_file:
        message = text_file.read()
    return message

def failed_log(profile_url):
    with open('failed_log.txt', 'a') as text_file:
        text_file.write(f'{profile_url}\n')        


            
