BEGIN {
  count = 0
}
{
  printf("%s",substr($0,1,length($0)-1))
  count += 1
  if (count == 2) {
    printf("\n")
    count = 0
  }
}
