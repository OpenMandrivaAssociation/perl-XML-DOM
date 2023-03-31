%define modname	XML-DOM
%define modver	1.46

Summary:	XML::DOM - build DOM Level 1 compliant document structures
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-libxml-perl >= 0.07
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
Provides:	perl-libxml-enno = %{version}-%{release}

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# some old'ish utf8 stuff, nuke it (rgs)
rm -f t/dom_jp_attr.t
rm -f t/dom_jp_cdata.t
rm -f t/dom_jp_example.t
rm -f t/dom_jp_minus.t
rm -f t/dom_jp_modify.t
rm -f t/dom_jp_print.t
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/XML/DOM
%{perl_vendorlib}/XML/DOM.pm
%{perl_vendorlib}/XML/DOM/*.pod
%{perl_vendorlib}/XML/DOM/*.pm
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man3/*

