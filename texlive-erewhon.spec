Name:		texlive-erewhon
Version:	70759
Release:	1
Summary:	Font package derived from Heuristica and Utopia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/erewhon
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Erewhon is based on the Heuristica package, which is based in
turn on Utopia. Erewhon adds a number of new features -- small
caps in all styles rather than just regular, added figure
styles (proportional, inferior, numerator, denominator) and
superior letters. The size is 6% smaller than Heuristica,
matching that of UtopiaStd.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/erewhon
%{_texmfdistdir}/fonts/vf/public/erewhon
%{_texmfdistdir}/fonts/type1/public/erewhon
%{_texmfdistdir}/fonts/tfm/public/erewhon
%{_texmfdistdir}/fonts/opentype/public/erewhon
%{_texmfdistdir}/fonts/map/dvips/erewhon
%{_texmfdistdir}/fonts/enc/dvips/erewhon
%{_texmfdistdir}/fonts/afm/public/erewhon
%doc %{_texmfdistdir}/doc/fonts/erewhon

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
