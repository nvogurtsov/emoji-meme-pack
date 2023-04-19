import yaml
import requests

config = 'config.yaml'

if __name__ == '__main__':
    with open(config, "r") as stream:
        emoji_yaml = yaml.safe_load(stream)
        emojis = emoji_yaml['emojis']

        for emoji in emojis:
            url = emoji['src']

            out_file = open("res/" + emoji['name'] + ".jpg", 'wb')
            response = requests.get(url)
            if response.status_code != 200:
                print(emoji)
            else:
                out_file.write(response.content)
                out_file.close()

