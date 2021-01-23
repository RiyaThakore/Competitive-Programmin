s='i.like.this.program'
words=s.split('.')
rev=''
for i in range(len(words)):
  rev+=words[len(words)-(i+1)]
  rev+='.'
print(rev)
