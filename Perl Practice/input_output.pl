use strict;
use warnings;



print('Enter two numbers');
my $var1 = <STDIN>;
my $var2 = <STDIN>;

print("Swapping both the nubers with each other");

($var1, $var2) = ($var2, $var1);

printf("Both the numbers are swapped and are = %d and %d", $var1, $var2);

