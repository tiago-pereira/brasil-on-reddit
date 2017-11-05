# BOT CONFIGURATION OPTIONS

# Bot user agent
USER_AGENT = 'A bot that runs r/BrasilOnReddit. Created by u/Synergix for PortugalOnReddit, forked by u/tasey.'

# Subreddit where the bot will post
SUBREDDIT_TO_POST = 'BrasilOnReddit'

# Expressions to monitor for
EXPRESSIONS_TO_MONITOR = ['brasil', 'brazil']

# Subreddits to monitor for (+ to monitor multiple subreddits; - to exclude a subreddit)
SUBREDDITS_TO_MONITOR = 'all-BrasilOnReddit-brasil-a7arte-AJS_BR-Ajuda-AjudaBrasil-artebrasileira-batepapo-BeloHorizonte-bestofbrasil-Bolsonaro-Bovespa-br4r-brasil2-brasil420-brasil_drama-Brasilandia-Brasilball-BrasilBitcoin-brasildemocratico-BrasildoB-brasilivre-brasilpics-brazilianmusic-brdev-BRSExplica-brugal-carreiras-ciencias-CinemaBrasil-circojeca-concursospublicos-Corinthians-craftmybox-curitiba-desabafos-Dota2BRa-Dota2Brasil-Escalada-EscritoresBrasil-eu_nvr-filmes-filmeseseries-foradecasa-futebol-g1comments-Gambiarra-gororoba-investimentos-jogatina-jogos-leagueoflegendsbrazil-Libertarianismo-linuxbrasil-Livros-maconha-Maromba-masqueporra-medoiosoio-merdasbrasildiz-Monarquia-motoca-MUSICA-musicanova-naoesensacionalista-NerdPowerBR-oBitcoin-palmeiras-Parana-PokemonGOBrasil-Portuguese-Psicanalise-Recife-riodejaneiro-riograndedosul-saopaulo-Semeando-southamerica-territoriolivre-tiodopave-veganismobrasil-youtubebrasil-ZeroQuatroMidia'

# Number of submissions to check in each run
SEARCH_LIMIT = 8000

# Blacklist, disconsider posts that contains all of the words of a index
BLACKLIST = ['brazile', 'brazille', 'brasile', 'brasille']

# Wait time between runs (in minutes)
WAIT_TIME = 15

# Post mode (choose 'direct' or 'comment')
# 'direct' will make the bot post the direct link of the source submission
# 'comment' will make the bot post the link to the comment section of the source submission
POST_MODE = 'comment'

# Required score to cross-post a submission found by search when setting up your subreddit
REQUIRED_SCORE = 500
