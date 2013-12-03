use v5.14;
use Data::Dumper;

my $file = shift;

open(my $fh, "<", $file) or die "We need a file!";
my $firstline = <$fh>;
close($fh);

my %puzzle_hash;

my @puzzle = split(/\s/,$firstline);

populate_hash();
eliminate("Z", "F");
eliminate("H", "A");
eliminate("T", "K");
eliminate("J", "E");
eliminate("F", "S");


print Dumper \%puzzle_hash;
sub populate_hash{
	open(my $dh, "<", 'words') or die "Where's your dictionary?!";
	foreach(@puzzle){
		$puzzle_hash{$_} = [];
	}
	while(my $word = <$dh>){
		chomp $word;
		my $pattern = pattern($word);
		for my $key (keys %puzzle_hash){
			if(length($key) eq length($pattern)){
				if(pattern($key) eq $pattern){
					push($puzzle_hash{$key}, uc($word));
				}
			}
		}
	}
}

sub pattern{
	my @alphabet = "A" .. "Z";
	my $word = shift;
	my $pattern = "";
	my %pattern_hash;
	chomp $word;
	for my $letter (split(//, $word)){
		if($letter eq '\''){
			$pattern .= '\'';
		}elsif($pattern_hash{$letter}){
			$pattern .= $pattern_hash{$letter};
		}else{
			$pattern_hash{$letter} = shift @alphabet;
			$pattern .= $pattern_hash{$letter};
		}

	}
	return $pattern;
}

sub eliminate{
	my ($encrypted_letter, $plaintext_letter) = @_;
	my $pos;
	for my $key(keys %puzzle_hash){
		while($key =~ /($encrypted_letter)/g){
			$pos = (pos ($key)) - 1;
			for my $word(@{$puzzle_hash{$key}}){
				if(substr($word, $pos, 1) eq $plaintext_letter){
					#keep the word
				}else{
					my @array = grep {!/$word/}  @{$puzzle_hash{$key}};
					$puzzle_hash{$key} = \@array;
				}

			}
		}
	}
}
