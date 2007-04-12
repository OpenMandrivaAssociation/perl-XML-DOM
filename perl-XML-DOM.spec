%define real_name XML-DOM

Summary:	XML::DOM - build DOM Level 1 compliant document structures
Name:		perl-%{real_name}
Version:	1.44
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-libxml-perl >= 0.07
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# some old'ish utf8 stuff, nuke it (rgs)
rm -f t/dom_jp_attr.t
rm -f t/dom_jp_cdata.t
rm -f t/dom_jp_example.t
rm -f t/dom_jp_minus.t
rm -f t/dom_jp_modify.t
rm -f t/dom_jp_print.t
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/XML/DOM
%{perl_vendorlib}/XML/DOM.pm
%{perl_vendorlib}/XML/DOM/*.pod
%{perl_vendorlib}/XML/DOM/*.pm
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man3/*

