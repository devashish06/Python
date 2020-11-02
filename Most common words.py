import collections
class Solutions:
  def mostCommonWord(self,paragraph: int, banned:List[str])->str:
    paragraph=paragraph.replace(","," ").replace(";"," ").replace("!"," ").replace("/"," ").replace("'"," ")
    arr=paragraph.lower().split()
    cntPara=collections.Counter(arr)
    tr=OrderedDict(cnt.Para.most_common())
    for i in tr.keys():
      if i not in banned:
      return i
