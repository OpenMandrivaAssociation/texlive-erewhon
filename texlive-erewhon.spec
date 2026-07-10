%global tl_name erewhon
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.123
Release:	%{tl_revision}.1
Summary:	Font package derived from Heuristica and Utopia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/erewhon
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Erewhon is based on the Heuristica package, which is based in turn on
Utopia. Erewhon adds a number of new features -- small caps in all
styles rather than just regular, added figure styles (proportional,
inferior, numerator, denominator) and superior letters. The size is 6%
smaller than Heuristica, matching that of UtopiaStd.

