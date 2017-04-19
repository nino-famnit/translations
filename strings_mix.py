##########################################################################
# Shkruaje ni funksion emphasise(title) qe e merr ni titull dhe e kthen ni
# fjale t're ku titulli ka me qene i theksuar, do te thote te gjitha
# shkronjat kane me qene t'mdhaja edhe t'ndane me hapesira. Hapesirat ne 
# ket' titull duhen me u trajtu ne te njejten menyre si dhe simbolet tjera 
# (do te thote shnderrohen ne hapesira t'trefishta).
#
# Shembull:
#
#     >>> emphasise('Breaking news')
#     'B R E A K I N G   N E W S'
##########################################################################
 


##########################################################################
# Shkruaje ni funksion emphasise_marked(title) qe e kthen ni fjale t're ku
# vetem ato shkronja mes simboleve * kane me qene t'shnderruara n't'mdhaja.
# Simbolet * duhet me i heq nga fjala e re.
#
# Example:
#
#     >>> emphasise_marked('Breaking *news* on Donald *Trump*')
#     'Breaking NEWS on Donald TRUMP'
##########################################################################




###########################################################################
# Shkruaje ni funksion is_palindrome(s) qe ka me e kthy vleren True nese 
# fjala s ka me qene palindrom dhe False nese nuk asht.
#
# Shembull:
#
#     >>> is_palindrome('neradodaren')
#     True
#     >>> is_palindrome('math')
#     False
############################################################################



############################################################################
# Ne thojme qe nje fjale asht gati palindrom nese duhet me e fshi saktesisht
# simbol nga ajo fjale qe me e pas ni palindrom. Fjala kolo per shembull asht 
# gati palindrom, se na duhet veq me fshi shkronjen k per me fitu fjalen olo.
#
# Shkruaje ni funksion almost_palindrome(s) qe ka me kthy True nese fjala s
# asht gati palindrom.
#
# Shembull:
#
#     >>> almost_palindrome('kolo')
#     True
#     >>> almost_palindrome('famnit')
#     False
##########################################################################



##########################################################################
# Ne thojme qe ni fjale asht pseudo-palindrom nese na duhet me e shtu ose me
# e fshi saktesisht vetem ni shkronje ose me e zevendesu me ni tjeter, qe me 
# e fitu ni palindrom. Shembuj:
#
# * robot (zevendeso t me r)
# * jana (shto shkronjen j n'fund)
#
# Shkruaje ni funksion pseudo_palindrome(s) qe ka me e kthy True atehere dhe 
# vetem  atehere kur fjala s asht palindrom.
#
# Example:
#
#     >>> pseudo_palindrome('robot')
#     True
#     >>> pseudo_palindrome('famnit')
##########################################################################




