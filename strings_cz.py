##########################################################################
# Napište funkci emphasise(title) která bere string title a vrací nový string
# kde je titulek zdůrazněn, tzn. všechny všechna písmena jsou velkými a 
# odděleny mezerami. S mezery v nadpisu stringu by mělo být zacházeno stejně 
# jako s jinými písmeny (stávají se trojitými mezerami). 
#
# Příklad:
#
#     >>> emphasise('Breaking news')
#     'B R E A K I N G   N E W S'
##########################################################################



##########################################################################
#Napište funkci emphasise_marked(title) která navrátí nový string ve kterém
# pouze písmena, která jsou mezi znaky * v originálním nadpisu převedená do
# velkých písmen. Znaky * by měli být odstraněny z vycházejícího stringu
#
# Příklad:
#
#     >>> emphasise_marked('Breaking *news* on Donald *Trump*')
#     'Breaking NEWS on Donald TRUMP'
##########################################################################



##########################################################################
# Napište funkci is_palindrome(s) která navrací True pokud string s je 
# palindrom a False pokud jím není.
#
# Příklad:
#
#     >>> is_palindrome('neradodaren')
#     True
#     >>> is_palindrome('math')
#     False
##########################################################################



##########################################################################
# Můžeme říci, že string je téměř palindrome pokud musíme smazat přesně
# jeden znak aby jsme z něj získali palindrome. Slovo kolo je téměř 
# palindrome, protože potřebujeme pouze smazat písmeno k k získání olo.
#
# Napište funkci almost_palindrome(s) která navrací True pokud je string s 
# téměř palindrom.
#
# Příklad:
#
#     >>> almost_palindrome('kolo')
#     True
#     >>> almost_palindrome('famnit')
#     False
##########################################################################



##########################################################################
# Říkáme, že string je pseudo-palindrome, pokud potřebujeme přidat nebo smazat
# přesně jedno písmeno anebo ho nahradit jiným, abychom získali palindrom. 
# Příklady: 
#
# * robot (nahradíme t písmenem r)
# * jana (přidáme písmeno j na konci)
#
# Napište funkci pseudo_palindrome(s) která navrací true pokud a pouze pokud 
# string s je pseudo-palindrom.
#
# Příklad:
#
#     >>> pseudo_palindrome('robot')
#     True
#     >>> pseudo_palindrome('famnit')
##########################################################################


