#!usr/bin/perl
$_="saya  lapar , belum makan- makan";
s/\s+/ /g;
s/\s+-|-\s+/-/g;
s/\s+,/, /g;
s/\s+\./\./g;
print;

while(@info=getpwent){
	if ($info[0]=~/^[a-z]\d+/){
	        $var = $info[0];  	##nrp
	        $var =~ s/m|c|d|y|x|e|g|b|a//g;
		$var2 = $info[6]; 	##nama
		$var2 =~ s/(\w+)/\L\u$1/g;
	        print "$var;$var2\n";
		## or
		#$nama =~ tr/[A-Z]/[a-z]/;
		#$nama =~ s/(\w+)/\u$1/g;
		## or
		##$nama=~s/\b(\w)/\U$1/g;
		##$nama =~ s/\b(.)/\U$1/g;
	}
}
