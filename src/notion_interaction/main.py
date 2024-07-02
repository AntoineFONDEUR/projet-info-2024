# %%
import requests

# %%
NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_API_KEY = "secret_3lW3pscXNMTLyVt8ucguorEg8Zrtld5rOo04jLOD43o"
DATABASE_ID_REP_TRAITE = "6fb0749269924363afa68bd3fab90fa2"

def add_to_notion(data):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "parent": {"database_id": DATABASE_ID_REP_TRAITE},
        "properties": {
            k: {"rich_text": [{"text": {"content": str(data[k])}}]} for k in data.keys()
        }
    }
    print(payload)

    requests.post(NOTION_API_URL, json=payload, headers=headers)

# %%
DATABASE_ID_DATA_BRUT = "d6e83d295d2c40548fdc0fa0241a24c4"

def get_form_rep_from_notion():
    NOTION_QUERY_URL = f"https://api.notion.com/v1/databases/{DATABASE_ID_DATA_BRUT}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(NOTION_QUERY_URL, headers=headers)
    data = response.json()

    rows = []
    for result in data['results']:
        properties = result['properties']
        en_tant_que = properties['Rep1']['rich_text'][0]['text']['content']
        jaimerais = properties['Rep2']['rich_text'][0]['text']['content']
        afin_de_parce_que = properties['Rep3']['rich_text'][0]['text']['content']
        rows.append([en_tant_que, jaimerais, afin_de_parce_que])

    return rows

# %%
get_form_rep_from_notion()

# %%
