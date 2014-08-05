import sys

from tfidf import *


def test_get_text(tmpdir):
	xml = \
"""<?xml version="1.0" encoding="iso-8859-1" ?>
<newsitem itemid="99" id="root" date="1996-10-21" xml:lang="en">
<title>Cats Do Hip Hop</title>
<dateline>USA 1996-10-21</dateline>
<text>
<p>Check this out.</p>
<p>Hilarious.</p>
</text>
<link>http://www.huffingtonpost.co.uk/2014/06/06/kittens-dance-turn-it-down-for-what_n_5458093.html</link>
<metadata>
<codes class="bip:countries:1.0">
  <code code="USA">
    <editdetail attribution="Cat Reuters BIP Coding Group" action="confirmed" date="1996-10-21"/>
  </code>
</codes>
<dc element="dc.date.created" value="1996-10-21"/>
<dc element="dc.source" value="Cat Reuters"/>
</metadata>
</newsitem>"""
	fullpath = tmpdir.dirname+"/"+tmpdir.basename+"/cat.xml"
	xmlfile = open(fullpath, "w")
	xmlfile.write(xml)
	xmlfile.close()
	expecting = ['Cats', 'Do', 'Hip', 'Hop', 'Check', 'this', 'out.', 'Hilarious.']
	result = get_text(fullpath)
	result.strip()
	result = re.sub('[\n ]+',' ',result)
	result = result.strip()
	result = result.split(" ")
	assert expecting == result

def test_empty_word_list():
	text = "  "
	expecting = []
	assert expecting == words(text)

def test_simple_word_list():
	text = "a big big cat dog big cat, the, 3.4 a."
	expecting = ['big', 'big', 'cat', 'dog', 'big', 'cat', 'the']
	assert expecting == words(text)

def test_words():
	text = """
	BELGIUM: EU sets ewe advance. The European set the second ewe premium
	advance for farmers on Friday at 5.462 Ecus per ewe, an European Union
	(EU) official said on Monday. "The first ewe premium -- paid in June --
	was 6.902 Ecus per ewe and the estimated figure for the year now stands
	at 18.206 Ecus per ewe," the official said. The premium is currently
	based on an average price of 355 Ecus per 100 kilo for lamb meat which
	is 21 higher than last year when the final premium figure paid
	in February was 24.821 Ecus per ewe. -- John White, Brussels Newsroom
	+32 2 287 6800
	"""
	expecting = ['belgium', 'sets', 'ewe', 'advance', 'the', 'european',
				 'set', 'the', 'second', 'ewe', 'premium', 'advance',
				 'for', 'farmers', 'friday', 'ecus', 'per', 'ewe',
				 'european', 'union', 'official', 'said', 'monday',
				 'the', 'first', 'ewe', 'premium', 'paid', 'june',
				 'was', 'ecus', 'per', 'ewe', 'and', 'the',
				 'estimated', 'figure', 'for', 'the', 'year',
				 'now', 'stands', 'ecus', 'per', 'ewe', 'the',
				 'official', 'said', 'the', 'premium', 'currently',
				 'based', 'average', 'price', 'ecus', 'per', 'kilo',
				 'for', 'lamb', 'meat', 'which', 'higher',
				 'than', 'last', 'year', 'when', 'the', 'final',
				 'premium', 'figure', 'paid', 'february', 'was',
				 'ecus', 'per', 'ewe', 'john', 'white', 'brussels',
				 'newsroom']
	result = words(text)
	assert expecting == result


def test_simple_index(tmpdir,capsys):
	xml = """
		<newsitem>
		<title>Premium price set</title>
		<text>
		<p>the official said and the premium was currently based on an average price.</p>
		</text>
		</newsitem>
	"""
	fullpath1 = tmpdir.dirname + "/" + tmpdir.basename + "/1.xml"
	save(xml, fullpath1)
	xml = """
		<newsitem>
		<title>German consumer confidence rises </title>
		<text>
		<p>he said consumer confidence index was unchanged in September and rose one percent on.</p>
		</text>
		</newsitem>
	"""
	fullpath2 = tmpdir.dirname + "/" + tmpdir.basename + "/2.xml"
	save(xml, fullpath2)
	(tf_map, df) = create_indexes([fullpath1, fullpath2])
	tf_map = simplify_tf_map(tf_map)
	map1 = tf_map[fullpath1]
	expected = Counter({'premium': '0.1429', 'price': '0.1429', 'the': '0.1429', " \
			   "'and': '0.0714', 'set': '0.0714', 'official': '0.0714', 'said': '0.0714', " \
			   "'currently': '0.0714', 'based': '0.0714', 'was': '0.0714', 'average': '0.0714'})
	assert map1 == expected
	map2 = tf_map[fullpath2]
	expected = Counter({'confidence': '0.1333', 'consumer': '0.1333', 'and': '0.0667', " \
			   "'index': '0.0667', 'said': '0.0667', 'german': '0.0667', 'rose': '0.0667', " \
			   "'unchanged': '0.0667', 'percent': '0.0667', 'one': '0.0667', " \
			   "'september': '0.0667', 'rises': '0.0667', 'was': '0.0667'})
	assert map2 == expected
#	(out,err) = capsys.readouterr()

################# SUPPORT CODE #################

def simplify_tf_map(tf_map):
	simpler = {}
	for f in tf_map:
		simpler[f] = simplify_tf(tf_map[f])
	return simpler

def simplify_tf(tf):
	simpler = Counter()
	for t in tf:
		simpler[t] = "%1.4f" % tf[t]
	return simpler

def save(xml, fullpath):
	xmlfile = open(fullpath, "w")
	xmlfile.write(xml)
	xmlfile.close()
