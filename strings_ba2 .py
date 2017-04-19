##########################################################################
# Napišite funkciju emphsise(title) koja od stringa naslova pravi novi string u kome je naslov    # naglašen, tj., sva slova su velika i razdvojena. Razmak između stringova naslova treba da se    # tretira na isti način kao i ostali karakteri.
#
# Primjer:
#
# >>> emphasise('Breaking news')
#    'B R E A K I N G   N E W S'
##########################################################################


##########################################################################
# Napišite funkciju emphasise_marked(title) koja vraća novi string, u kome su samo ona slova koja # su između karaktera * u orginalnom naslovu, konvertovana u velika slova. Karakter * bi trebao   # biti obrisan u rezultujućem (novom) stringu.
#
# Primjer: 
#
# >>> emphasise_marked('Breaking *news* on Donald *Trump*')
#    'Breaking NEWS on Donald TRUMP
##########################################################################


##########################################################################
# Napišite funkciju is_palindrome(s) koja izbacuje True ako je string palidrom i False ako nije.
#
# Primjer:
#
# >>> is_palindrome('neradodaren')
#    True
# >>> is_palindrome('math')
#    False
##########################################################################



##########################################################################
# Kažemo da je string skoro pa palindrom ako obrišemo jedan karakter iz stringa da bismo dobili   # palindrom. Riječ kolo je skoro palindrom, zato što je potrebno samo obrisati slovo k da bismo   # dobili olo.
#
# Napišite funkciju almost_palindrome(s) koja pokazuje True ako je string skoro palindrom.
#
# Primjer: 
#
# >>> almost_palindrome('kolo')
#     True
# >>> almost_palindrome('famnit')
#     False
##########################################################################



##########################################################################
# Kažemo da je string pseudo-palindrom ako treba da dodamo ili obrišemo tačko jedno slovo ili ga  # zamijenimo drugim da bismo dobili palindrom. Primjeri:
#
# * robot (zamijeni t sa r)
# * jana (dodaj slovo j na kraju)
#
# Napišite funkciju pseudo-palindrome(s) koja pokazuje True ako i samo ako je string pseudo-      # palindrome.
#
# Primjer:
#
# >>> pseudo_palindrome('robot')
#     True
# >>> pseudo_palindrome('famnit')
##########################################################################



