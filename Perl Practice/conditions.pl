use strict;
use warnings;

print "Enter your age, name and license as (YES/NO)";

chomp(my $age = <STDIN>);
chomp(my $name = <STDIN>);
chomp(my $lic_status = <STDIN>);

#Conditions check

if( $age > 16 && ($lic_status eq 'YES' || $lic_status eq 'yes')){
	printf("%s can drive the Scooter", $name); 
}elsif( $age > 16 && ($lic_status eq 'NO' || $lic_status eq 'no')){
	printf("%s , please apply for your license", $name);
}else{
	printf("%s , can not drive vehicle", $name);
}


