import json

data = None
# load JSON data from file
with open("wordings.json", "r") as file:
    data = json.load(file)

print(len(data))

# check if key exists
for i in range(len(data)):
    del data[i]["id"]
    del data[i]["word_diff_categories_id"]
    del data[i]["img"]
    del data[i]["image_url"]
    del data[i]["category"]


def convert_words_to_array(data):
    """
    將 tw_word 和 cn_word 欄位從字串轉換為陣列格式
    使用 "/" 作為分隔符
    """
    converted_data = []

    for item in data:
        # 創建新的字典來存放轉換後的資料
        new_item = {
            "tw_word": (
                item["tw_word"].split("/")
                if "/" in item["tw_word"]
                else [item["tw_word"]]
            ),
            "cn_word": item["cn_word"].split("/"),
            "type": item["type"],
        }
        converted_data.append(new_item)

    return converted_data


converted_data = convert_words_to_array(data)


# Write the updated json to json file
with open("output.json", "w") as f:
    # write updated data
    json.dump(converted_data, f, indent=2, ensure_ascii=False)
