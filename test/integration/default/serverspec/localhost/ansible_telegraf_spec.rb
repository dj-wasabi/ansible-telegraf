require 'serverspec'
require 'spec_helper'

describe 'Telegraf Packages' do
    describe package('telegraf') do
        it { should be_installed }
    end
end


describe 'Telegraf Services' do
    describe service('telegraf') do
        it { should be_enabled }
    end
end

describe 'Telegraf Configuration' do
    describe file('/etc/opt/telegraf/telegraf.conf') do
        it { should be_file}
        it { should be_owned_by 'root'}
        it { should be_grouped_into 'root'}

        it { should contain "[cpu]" }
        it { should contain "[mem]" }
        it { should contain "url = \"http://localhost:8086\"" }
    end
end
