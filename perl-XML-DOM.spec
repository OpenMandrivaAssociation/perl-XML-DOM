%define upstream_name    XML-DOM
%define upstream_version 1.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	XML::DOM - build DOM Level 1 compliant document structures
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-libxml-perl >= 0.07
BuildArch:	noarch
Provides:	perl-libxml-enno = %{version}-%{release}

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.440.0-4mdv2012.0
+ Revision: 765835
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.440.0-2
+ Revision: 667414
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.440.0-1mdv2011.0
+ Revision: 402538
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.44-7mdv2009.1
+ Revision: 351690
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.44-6mdv2009.0
+ Revision: 224609
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.44-5mdv2008.1
+ Revision: 180649
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.44-4mdv2008.0
+ Revision: 63023
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.44-3mdv2008.0
+ Revision: 23248
- rebuild


* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 1.44-2mdk
- Rebuild
- use mkrel

* Thu Jul 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.44-1mdk
- 1.44

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.43-1mdk
- initial Mandriva package

