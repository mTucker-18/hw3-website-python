
# This code recombines a content html with the base html to make a new, working, html file
# for those pages in the docs/ folder

def main():
    pages = import_json()
    for item in pages:
        base_html = open('templates/base.html').read() # read in the entire template    
              
        complete_page = replace_placeholders(base_html, item) #invoke replace function
  
        open(item['output_file'], 'w+').write(complete_page)


#   This function replaces all placeholders with correct items within the pages

def replace_placeholders(base_webpage, item):
    content_html = open(item['file_name']).read() # read in the content of the current html page
    
    base_webpage = \
                    base_webpage.replace('{{content}}', content_html)\
                                .replace('{{title}}', item['title'])\
                                .replace('{{opening_text}}', item['opening_text'])\
                                .replace('{{sub_text}}', item['sub_text'])
    return base_webpage
    
    
# This function imports my list of dictionaries as 'pages', in order to edit/add new items
# to the templates, add them in the dictionaries.json document    
    
def import_json():
    import json
    json_string = open('dictionaries.json').read()
    pages_json = json.loads(json_string)
    return pages_json


if __name__ == '__main__':
    main()
    
