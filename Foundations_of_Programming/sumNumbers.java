/*
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
*/

public int sumNumbers(String str) {
  String numStr = "";
  int result = 0;
  str += 's';	// for ending edge case
  char[] s = str.toCharArray();
  
  for (int i=0; i < s.length; i++) {
    if (Character.isDigit(s[i])) numStr += s[i];
    else if (numStr.length() != 0) {
      result += Integer.parseInt(numStr);
      numStr = "";
    }
  }
  return result;
}
