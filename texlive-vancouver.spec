# revision 25519
# category Package
# catalog-ctan /biblio/bibtex/contrib/vancouver
# catalog-date 2012-02-27 00:21:15 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-vancouver
Version:	20120227
Release:	7
Summary:	Bibliographic style file for Biomedical Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/vancouver
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This BibTeX style file is generated with the docstrip utility
and modified manually to meet the Uniform Requirements for
Manuscripts Submitted to Biomedical Journals as published in N
Engl J Med 1997;336:309-315 (also known as the Vancouver
style). The complete set of requirements may be viewed on the
ICMJE web site.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/vancouver/vancouver.bst
%doc %{_texmfdistdir}/doc/bibtex/vancouver/FAQ
%doc %{_texmfdistdir}/doc/bibtex/vancouver/README
%doc %{_texmfdistdir}/doc/bibtex/vancouver/vancouver.bib
%doc %{_texmfdistdir}/doc/bibtex/vancouver/vancouver.pdf
%doc %{_texmfdistdir}/doc/bibtex/vancouver/vancouver.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 20120227-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120227-1
+ Revision: 783097
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070313-2
+ Revision: 757361
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070313-1
+ Revision: 719870
- texlive-vancouver
- texlive-vancouver
- texlive-vancouver

