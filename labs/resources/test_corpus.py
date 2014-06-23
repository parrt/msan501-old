from tfidf import *
import sys

if __name__ == '__main__':
	files = filelist(sys.argv[1])
	# On, the next line to test just the first 100 files instead of all files
	# files = files[:100]
	N = len(files)
	print N, "files"

	(file_to_histo, word_to_numdocs) = create_indexes(files)
	for f in files:
		tfmap = doc_tfidf(file_to_histo[f], word_to_numdocs, N)
		# convert map to a Counter object so we can use most_common()
		term_pair = Counter(tfmap).most_common(1)[0]
		print os.path.basename(f), "(%s, %1.4f)" % (term_pair[0], term_pair[1])