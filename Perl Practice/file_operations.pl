#Program for understanding file operations

use strict;
use warnings;
use IO::File;

#Creating a new File object 

#my $FH = IO::File->new('test_file.txt','r') or die("Can not create an file abject : $!");
#if( defined $FH ) {
#	print <$FH>;
#	undef $FH;
#}
	
open(FH,'< test_file.txt') or die("Can not open a file : $!");
while(<FH>){
	my $line = $_;
	chomp($line);
	if( $line =~ m/DIGIT/){
		print("$line \n");
	}
}
close(FH);