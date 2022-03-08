# Things To Work On

* Main window
  * [x] Library buttons - Errors out when clicked and no library is selected.
  * [x] Library view - Needs to scroll back to top when switching libraries.
  * [ ] Add library/settings buttons get cut off on the right side when hovering.
  * [ ] Some sort of indicator for series that need to be updated?
  * [ ] A way to manually edit a series and maintain that through future updating.

* Add Library Dialog
  * [ ] Callback - Should probably improve how the name of the new library gets sent back.
  * [ ] Cover image downloading - incorporate into loading bar and only download images that don't already exist.

* Update Library Dialog
  * [ ] Display info about which series actually got updated, not just the entire list of ongoing series.

* Web scraper
  * [ ] Redo scraper because MU removed their json header type option on the search page.
  * [ ] Find improperly matched series and update edge cases.
  * [ ] Tweak the fuzzy string matching to better match series.

* Directory scanner
  * [x] Parse out the volume number and maintain a list for each series.
  * [x] Check for omnibuses and other edition types
  * [ ] Multi-volume files - maybe?
  