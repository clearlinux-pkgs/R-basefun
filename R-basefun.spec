#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-basefun
Version  : 1.1.3
Release  : 10
URL      : https://cran.r-project.org/src/contrib/basefun_1.1-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/basefun_1.1-3.tar.gz
Summary  : Infrastructure for Computing with Basis Functions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-basefun-lib = %{version}-%{release}
Requires: R-orthopolynom
Requires: R-polynom
Requires: R-variables
BuildRequires : R-orthopolynom
BuildRequires : R-polynom
BuildRequires : R-variables
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-basefun package.
Group: Libraries

%description lib
lib components for the R-basefun package.


%prep
%setup -q -c -n basefun
cd %{_builddir}/basefun

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653489328

%install
export SOURCE_DATE_EPOCH=1653489328
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library basefun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library basefun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library basefun
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc basefun || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/basefun/CITATION
/usr/lib64/R/library/basefun/DESCRIPTION
/usr/lib64/R/library/basefun/INDEX
/usr/lib64/R/library/basefun/Meta/Rd.rds
/usr/lib64/R/library/basefun/Meta/features.rds
/usr/lib64/R/library/basefun/Meta/hsearch.rds
/usr/lib64/R/library/basefun/Meta/links.rds
/usr/lib64/R/library/basefun/Meta/nsInfo.rds
/usr/lib64/R/library/basefun/Meta/package.rds
/usr/lib64/R/library/basefun/NAMESPACE
/usr/lib64/R/library/basefun/NEWS.Rd
/usr/lib64/R/library/basefun/R/basefun
/usr/lib64/R/library/basefun/R/basefun.rdb
/usr/lib64/R/library/basefun/R/basefun.rdx
/usr/lib64/R/library/basefun/help/AnIndex
/usr/lib64/R/library/basefun/help/aliases.rds
/usr/lib64/R/library/basefun/help/basefun.rdb
/usr/lib64/R/library/basefun/help/basefun.rdx
/usr/lib64/R/library/basefun/help/paths.rds
/usr/lib64/R/library/basefun/html/00Index.html
/usr/lib64/R/library/basefun/html/R.css
/usr/lib64/R/library/basefun/tests/Bernstein-Ex.R
/usr/lib64/R/library/basefun/tests/Bernstein-Ex.Rout.save
/usr/lib64/R/library/basefun/tests/bases-Ex.R
/usr/lib64/R/library/basefun/tests/formula.R
/usr/lib64/R/library/basefun/tests/predict.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/basefun/libs/basefun.so
/usr/lib64/R/library/basefun/libs/basefun.so.avx2
/usr/lib64/R/library/basefun/libs/basefun.so.avx512
