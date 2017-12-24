# using dictionaries to translate counting to ten in Korean, Spanish, and Korean/Chinese (HanMun), and Japanese



korean = {'seven': 'ilgop', 'ten': 'yol', 'nine': 'yodol', 'six': 'yosot', 'three': 'set', 'two': 'dul', 'four': 'net', 'five': 'tasot', 'eight': 'ilgop', 'one': 'hana'}
chinese = {'four': 'sa', 'seven': 'chil', 'one': 'il', 'nine': 'gu', 'ten': 'ship', 'five': 'oh', 'six': 'nyuk', 'eight': 'pal', 'three': 'sam', 'two': 'ee'}
spanish = {'seven': 'sieta', 'ten': 'dias', 'nine': 'nueva', 'six': 'seis', 'three': 'tres', 'two': 'dos', 'four': 'quatro', 'five': 'cinco', 'eight': 'ocho', 'one': 'uno'}
japanese = {'four': 'shi', 'seven': 'shichi', 'one': 'ichi', 'nine': 'ku', 'ten': 'ju', 'five': 'go', 'six': 'roku', 'eight': 'hachi', 'three': 'san', 'two': 'ni'}
integer = {'7':'seven', '10':'ten', '9':'nine', '6':'six', '3':'three', '2':'two', '4':'four', '5':'five', '8':'eight', '1':'one'}

num = raw_input('translate the number: ')
if num in integer: num = integer[num]
if num in korean and num in spanish and num in chinese:
	print '\n',num.title(),'\n - Korean:',korean[num],'\n - Spanish:',spanish[num],'\n - Chinese:', chinese[num],'\n - Japanese:', japanese[num],'\n'
else:
	print '\nSorry, we don\'t have that one yet. Care to try again?\n'


#-----------------------------------------------------------------------------------#
# Below I am trying to do the same thing with a nested dict()

'''

counting = {'one':{'korean':'hana','chinese':'il','japanese':'ichi','spanish':'uno','integer':1},'two':{'korean':'dul','chinese':'i','japanese':'ni','spanish':'dos','integer':2},'three':{'korean':'set','chinese':'sam','japanese':'san','spanish':'tres','integer':3},'four':{'korean':'net','chinese':'sa','japanese':'she','spanish':'quatro','integer':4},'five':{'korean':'tasot','chinese':'oh','japanese':'go','spanish':'cinco','integer':5},'six':{'korean':'yosot','chinese':'nyuk','japanese':'roku','spanish':'seis','integer':6},'seven':{'korean':'ilgop','chinese':'ch\'il','japanese':'shichi','spanish':'sieta','integer':7},'eight':{'korean':'yodol','chinese':'p\'al','japanese':'hachi','spanish':'ocho','integer':8},'nine':{'korean':'ahop','chinese':'gu','japanese':'ku','spanish':'nueve','integer':9},'ten':{'korean':'yol','chinese':'ship','japanese':'ju','spanish':'dias','integer':10}}

num = 1
num in (counting['one'] or counting['two'] or counting['three'] or counting['four'] or counting['five'] or counting['six'] or counting['seven'] or counting['eight'] or counting['nine'] or counting['ten'])['integer']

'''