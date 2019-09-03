// 1. use str.replace()
public String withoutString(String base, String remove) {
  base = base.replace(remove.toUpperCase(), "");
  base = base.replace(remove.toLowerCase(), "");
  base = base.replace(remove, "");
  return base;
}

// 2. use recursion, indexOf, substring
public String withoutString(String base, String remove) {
	int remIdx = base.toLowerCase().indexOf(remove.toLowerCase());
	if (remIdx == -1) return base;
	return base.substring(0, remIdx) + withoutString(base.substring(remIdx+remove.length()), remove);
}