# https://github.com/tamccullough - questions? twitter @tamccullough
from flask import Flask,jsonify,request
import pandas as pd

# for this file to not be so long, I have placed a dictionary in the following py file
# to edit there. Saves some clutter in this area
import collection_func as cf

# edit this file however you see fit. If it suits you to make changes to it for your work. Do so.

# set the name for the collection
collection_name = 'Collection'

app = Flask(__name__)

# serve the json file metadata required for the token
@app.route('/<token_id>') # url includes the token_id number
def item(token_id):
    token_id = int(token_id)
    # data for the collection of images is stored in a csv file, loaded into a dataframe
    df = pd.read_csv(f'collection/collection_data.csv')
    # get the relevant slice from the dataframe, selecting from the token_id
    item = df.loc[token_id]
    # get the url root which will be printed for the nft reference
    url_path = request.url_root
    #external_url = 'https://testnets.opensea.io/assets/<asset_contract_address>/{token_id}'

    # taking the
    attributes = []
    for i in item.keys():
        if i in ['name','image']: # pass any column you have created that should not be an attribute
            pass
        else:
            attribute = {
                'trait_type':i,
                'value':cf.get_collection_item(i,item[i]) # using the dictionary found in collection_func get the appropriate strings
            }
            attributes.append(attribute)

    # using Flask jsonify to pass the selected data as json file format
    return jsonify({
        'name': item['name'],
        'external_url': f'{url_path}{token_id}',
        'image': f'{url_path}image/{token_id}',
        'description': f'{collection_name} that enjoys spreading the power of the Dark Lord.',
        'attributes': attributes,
    })

# serve the selected image, important for the image to show up within the nft
@app.route('/image/<token_id>')
def image(token_id):
    token_id = int(token_id)
    df = pd.read_csv(f'collection/collection_data.csv')
    item = df.loc[token_id]
    # if you haven't named your images using a lower case version of your collection name
    # you need to change the following string to point to the images
    image_url = f'collection/{collection_name.lower()}{token_id+1}.png'

    return send_file(image_url, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
