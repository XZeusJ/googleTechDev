// list.stream().mapToInt(Integer::intValue).toArray()

int[] sort(int[] a) {
  if (a.length <= 1) return a;
  
  ArrayList<Integer> result = new ArrayList<>();
  
  result.add(a[0]);
  for (int i = 1; i< a.length; i++) {
    if (a[i-1] != a[i]) result.add(a[i]);
  }
  
  return result.stream().mapToInt(Integer::intValue).toArray();
}
