# Changelog

## 0.2.0 
### Added
- `comp`
- `count`
- `count_`
- `identity`
- `reduce`
- `reduced`
- `threadf`
- `threadl`
- `trampoline`

### Changed
- `is_nested` now works with dictionaries


### Fixed
- `less_than` would return true for this `1 < 4 < 2` [issue #16](https://github.com/AbhinavOmprakash/functionali/issues/16) 
- `foldr` now works with iterators. [issues #17](https://github.com/AbhinavOmprakash/functionali/issues/17) 
- `curry` now works with 0-arg functions

## 0.1.1 Jul 27, 2021
### Fixed
- `first`, `second`, now work with iterables. 

## 0.1.0 Jul 26, 2021
### Added
- `all_predicates`
- `argmap`
- `argzip`
- `butlast`
- `complement`
- `concat`
- `conj`
- `cons`
- `contains`
- `curry`
- `drop`
- `drop_while`
- `equals`
- `ffirst`
- `fifth`
- `first`
- `flatten`
- `flip`
- `foldr`
- `fourth`
- `greater_than`
- `greater_than_eq`
- `insert`
- `interleave`
- `is_`
- `is_atom`
- `is_divisible`
- `is_divisible_by`
- `is_empty`
- `is_even`
- `is_nested`
- `is_numeric`
- `is_odd`
- `iter_`
- `last`
- `less_than`
- `less_than_eq`
- `remove`
- `rest`
- `reversed_second`
- `some_predicates`
- `split_with`
- `take`
- `take_while`
- `third`
- `unzip`