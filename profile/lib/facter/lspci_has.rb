require 'facter/util/virtual'

def lspci_match(regex)
  output = Facter::Util::Virtual.lspci
  matches = output.scan(regex)
  matches.flatten.reject {|s| s.nil?}.length
end

Facter.add(:lspci_has, :type => :aggregate) do
  confine :kernel => "Linux"

  chunk(:intel82599sfp) do
    count = lspci_match(/Intel.*82599ES.*SFP\+/)
    { "intel82599sfp" => count > 0 }
  end

end
