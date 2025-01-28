### DEPLOYMENT INSTRUCTIONS ###


## FOR DEPLOTMENT ##

1. set DEBUG = False
2. run - pip freeze > requirements.txt - locally
3. set up env variables
4. CORS?

ALLOWED_HOSTS?
## FOR DEV ##

1. set DEBUG = True





# Development notes


    
        consider pagifying through useffect the indexing of data
        
        for update and create handle the self issue regarding link display, thinking just parse it out on front
        

        Have log in and register clear any remaing cookies so there are no conflicts cookies

        revise how the form looks

        

        super user script on deployment?

        postgres amazon and aws



APU GUIDE BELOW


# -------------ADD ANIME DATA STURCTURE FOR CREATE AND UPDATE-----------------





# INDEX FILTER OPTIONS:
format should be in the format all text as seen plus requirement from parthesis
user [
        username
]
order_by [
        titleJpRoman(default requires order)
        updated_at
]
order [
        des(default)
        asc
]


### ANIME APIS ###
BASE_URL = '/anime/'

## simple list / index based calls
'index/base' - returns full list of all existing anime (organized by creation time descending)
'<int:id>/abbrv' - receives anime id and returns an abbreviated form of data for things like searching (fields = ['id', 'titleEnglish', 'titleJpRoman', 'image'])
'<int:id>' - recieves anime id an returns anime with full data

## create / update / delete based calls
'create' - anime creation call (see api guide above for input structure reference)
'<int:id>/update' - anime update call (see api guide above for input structure reference)
'<int:id>/delete' - recieves anime id and dels the cooresponding anime

## filtering / search based calls
'index/by' - receives parameters in the form {filter: 'filter string'} filter options ('order_by': 'field', 'order': 'order') returns all possible matches
'index/search' - receives parameters in the form {filter: 'filter string'} filter options (titleEnglish, titleJpRoman, idPre, idSeq) returns all possible matches



## anime adjacent calls

# studio calls
'studio/create' - studio creation call (see api guide above for input structure reference)
'studio/index' - simple list of all studios alphabetical order
'studio/delete/<int:studio_id>' - receives studio id and dels corresponding

# genre calls
'genre/create' - genre creation call (see api guide above for input structure reference)
'genre/index' - simple list of all genres alphabetical order
'genre/delete/<int:genre_id>' - receives genre id and dels corresponding



