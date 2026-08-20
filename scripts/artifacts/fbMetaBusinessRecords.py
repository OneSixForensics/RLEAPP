__artifacts_v2__ = {
    "meta_account_info": {
        "name": "Meta Business Record - Account Information",
        "description": "Account, profile and report information from a Meta Platforms "
                       "Business Record return (2026+ HTML format)",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "Parses the 2026+ 'Meta Platforms Business Record' HTML format "
                 "(minified t/o/i/m div classes). Legacy-format returns are handled "
                 "by the existing fbig* modules.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_account_info",
        "artifact_icon": "user",
    },
    "meta_ncmec_cybertips": {
        "name": "Meta Business Record - NCMEC CyberTips",
        "description": "NCMEC CyberTip reports associated with the account, including "
                       "uploaded media, upload IP and human-review status",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "One row per Text/Media ID within each CyberTip. Media referenced by "
                 "the report is linked from linked_media/ when present; absent files "
                 "are flagged, not dropped.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_ncmec_cybertips",
        "artifact_icon": "alert-triangle",
    },
    "meta_ip_addresses": {
        "name": "Meta Business Record - IP Addresses",
        "description": "IP address / port activity log for the account (logins, uploads, "
                       "session updates)",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "Source port (when captured) appears after the colon in the IP value.",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_ip_addresses",
        "artifact_icon": "globe",
    },
    "meta_group_messages": {
        "name": "Meta Business Record - Group Messages",
        "description": "Posts made by the account holder within Facebook groups, "
                       "including attachments",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "One row per attachment (posts without attachments get a single row). "
                 "Attachment media is linked from linked_media/ when present.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_group_messages",
        "artifact_icon": "message-circle",
    },
    "meta_videos": {
        "name": "Meta Business Record - Videos",
        "description": "Videos uploaded by the account holder, with upload IP and "
                       "privacy setting",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "Video media is linked from linked_media/ when present; absent files "
                 "are flagged, not dropped.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_videos",
        "artifact_icon": "video",
    },
    "meta_photos": {
        "name": "Meta Business Record - Photos",
        "description": "Photos uploaded by the account holder",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "Photo media is linked from linked_media/ when present.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_photos",
        "artifact_icon": "image",
    },
    "meta_devices": {
        "name": "Meta Business Record - Devices",
        "description": "Devices Info entries — devices used to access the account, with "
                       "family device IDs and first/last seen times",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_devices",
        "artifact_icon": "smartphone",
    },
    "meta_recognized_devices": {
        "name": "Meta Business Record - Recognized Devices",
        "description": "Devices/browsers the account holder approved as trusted",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_recognized_devices",
        "artifact_icon": "monitor",
    },
    "meta_cookies": {
        "name": "Meta Business Record - Machine Cookies",
        "description": "Machine cookies associated with the account — shows other "
                       "accounts sharing the same device/browser",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "The Users field lists every account seen with the cookie — "
                 "valuable for identifying shared devices.",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_cookies",
        "artifact_icon": "database",
    },
    "meta_friends": {
        "name": "Meta Business Record - Friends",
        "description": "Friends list at the time of production",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_friends",
        "artifact_icon": "users",
    },
    "meta_friend_requests": {
        "name": "Meta Business Record - Friend Requests",
        "description": "Friend requests sent or received by the account holder",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_friend_requests",
        "artifact_icon": "user-plus",
    },
    "meta_groups": {
        "name": "Meta Business Record - Groups",
        "description": "Facebook groups the account holder is a member of, with join dates",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_groups",
        "artifact_icon": "users",
    },
    "meta_support_correspondence": {
        "name": "Meta Business Record - Support Correspondence",
        "description": "Correspondence between the account holder and Facebook/Meta "
                       "(takedowns, appeals, authenticity checks)",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_support_correspondence",
        "artifact_icon": "mail",
    },
    "meta_payment_info": {
        "name": "Meta Business Record - Payment Information",
        "description": "Credit cards, PayPal accounts and direct debit records associated "
                       "with the account",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_payment_info",
        "artifact_icon": "credit-card",
    },
    "meta_linked_accounts": {
        "name": "Meta Business Record - Linked Accounts",
        "description": "Accounts on other Meta services (Instagram, Threads, Facebook) "
                       "linked to this account",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "",
        "paths": ('*/records.html', '*/preservation*.html'),
        "output_types": "standard",
        "function": "meta_linked_accounts",
        "artifact_icon": "link",
    },
    "meta_other_sections": {
        "name": "Meta Business Record - Other Sections",
        "description": "Generic field/value dump of every report section that is not "
                       "covered by a dedicated Meta Business Record artifact — nothing "
                       "in the return is silently dropped",
        "author": "@OneSixForensics, Claude",
        "version": "0.1",
        "date": "2026-07-15",
        "requirements": "none",
        "category": "Facebook - Instagram Returns",
        "notes": "Sections reporting 'No responsive records' are skipped. Fields are "
                 "shown in document order.",
        "paths": ('*/records.html', '*/preservation*.html', '*/linked_media/*'),
        "output_types": "standard",
        "function": "meta_other_sections",
        "artifact_icon": "list",
    },
}

# ---------------------------------------------------------------------------
# Meta Platforms Business Record (2026+ HTML format) parser.
#
# Around mid-2026 Meta changed the law-enforcement return format: the old
# verbose CSS classes (div_table outer/inner, most_inner) that the fbig*
# modules key on were replaced with minified classes:
#     .t = div table   .o = outer (one field)   .i = inner (label)
#     .m = most inner (value)                   .p = padding/line break
# Each field is:  <div class="t o"><div class="t i">LABEL<div class="m">VALUE
# </div></div></div>  and VALUE may recursively contain further "t o" blocks.
# Section anchors are unchanged: <div id="property-<name>" class="content-pane">.
#
# Print pagination inserts <div class="pageBreak"> markers anywhere — including
# mid-field — in which case the value continues in a follow-on block with an
# EMPTY label. The flattener below merges those continuations back onto the
# preceding field, which was validated against a real return where values,
# labels and even single timestamps were split across page boundaries.
# ---------------------------------------------------------------------------
import os
import re

from bs4 import BeautifulSoup

from scripts.ilapfuncs import artifact_processor, logfunc, check_in_media

_HTML_NAME = re.compile(r'^(records|preservation.*)\.html$', re.IGNORECASE)
_TS_UTC = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC$')

# Cache of parsed files: cleaned path -> {section_id: [(label, value), ...]}
# Artifact functions run sequentially in one process and each re-receives the
# same files; parsing a 0.5 MB HTML once instead of 16 times matters.
_parsed_cache = {}


def _clean_path(path):
    """Strip the Windows extended-length path prefix (\\\\?\\) if present."""
    p = str(path)
    return p[4:] if p.startswith('\\\\?\\') else p


def _ts(value):
    """'2025-11-06 07:33:25 UTC' -> '2025-11-06 07:33:25' for LAVA's
    fromisoformat conversion (naive values are treated as UTC; the column
    header carries the UTC label). Non-matching values pass through."""
    m = _TS_UTC.match(value.strip()) if value else None
    return m.group(1) if m else (value or '')


def _is_o(tag):
    cls = tag.get('class') or []
    return tag.name == 'div' and 'o' in cls and 't' in cls


def _parse_block(o_div):
    """Parse one 't o' field div -> (label, value); value is a string for a
    leaf or a list of child (label, value) tuples for nested records."""
    i_div = o_div.find('div', class_='i', recursive=False)
    if i_div is None:
        return ('', o_div.get_text(' ', strip=True))

    label_parts = []
    for child in i_div.children:
        if getattr(child, 'name', None) is None:
            t = str(child).strip()
            if t:
                label_parts.append(t)
        elif child.name == 'div' and 'm' in (child.get('class') or []):
            break
    label = ' '.join(label_parts)

    m_div = i_div.find('div', class_='m', recursive=False)
    if m_div is None:
        return (label, '')

    # Collect the top-most nested 't o' blocks inside the value (if any).
    top_os = []

    def walk(tag):
        for c in tag.children:
            if getattr(c, 'name', None) == 'div':
                if _is_o(c):
                    top_os.append(c)
                else:
                    walk(c)

    walk(m_div)
    if top_os:
        return (label, [_parse_block(o) for o in top_os])

    # Leaf: 'p' divs act as line separators inside a value.
    for p in m_div.find_all('div', class_='p'):
        p.replace_with('\n')
    val = m_div.get_text()
    val = re.sub(r'\n{2,}', '\n', val).strip()
    return (label, val)


def _flatten(nodes, out):
    """Depth-first leaves of the (label, value) tree, in document order."""
    for label, val in nodes:
        if isinstance(val, list):
            _flatten(val, out)
        else:
            out.append([label, val])


def _merge_continuations(leaves):
    """Merge page-break continuation leaves (empty label) into the preceding
    field: fill it if it was left empty, otherwise append on a new line."""
    merged = []
    for label, val in leaves:
        if label == '' and merged:
            if val == '':
                continue
            if merged[-1][1] == '':
                merged[-1][1] = val
            else:
                merged[-1][1] += '\n' + val
        else:
            merged.append([label, val])
    return [(l, v) for l, v in merged]


def _parse_html(cleaned_path):
    """Parse one records/preservation HTML into {section_id: [(label, value)]}.
    Returns None if the file is not the 2026+ Meta Business Record format."""
    if cleaned_path in _parsed_cache:
        return _parsed_cache[cleaned_path]

    try:
        with open(cleaned_path, encoding='utf-8', errors='replace') as fh:
            soup = BeautifulSoup(fh, 'html.parser')
    except (OSError, ValueError) as e:
        logfunc(f'Meta Business Record: cannot read {cleaned_path}: {e}')
        _parsed_cache[cleaned_path] = None
        return None

    if soup.find('div', class_='o') is None:
        # Legacy format (div_table/most_inner) — the fbig* modules handle it.
        logfunc(f'Meta Business Record: {os.path.basename(cleaned_path)} is not '
                f'the 2026+ format, skipping (legacy fbig* modules cover it).')
        _parsed_cache[cleaned_path] = None
        return None

    sections = {}
    for pane in soup.find_all('div', id=re.compile(r'^property-')):
        sec_id = pane.get('id')[len('property-'):]
        for pb in pane.find_all('div', class_='pageBreak'):
            pb.decompose()
        top = [c for c in pane.children if getattr(c, 'name', None) == 'div' and _is_o(c)]
        leaves = []
        _flatten([_parse_block(o) for o in top], leaves)
        pairs = _merge_continuations(leaves)
        # Drop the section's definition text (it is boilerplate, and its
        # page-break continuations were already merged into it).
        pairs = [(l, v) for l, v in pairs if not l.endswith(' Definition')]
        sections[sec_id] = pairs
    _parsed_cache[cleaned_path] = sections
    return sections


def _iter_reports(files_found):
    """Yield (basename, cleaned_path, sections_dict) for each parseable
    records/preservation HTML in files_found, in a stable order."""
    htmls = []
    for raw in files_found:
        cf = _clean_path(raw)
        if _HTML_NAME.match(os.path.basename(cf)):
            htmls.append(cf)
    for cf in sorted(set(htmls), key=lambda p: os.path.basename(p).lower()):
        sections = _parse_html(cf)
        if sections:
            yield os.path.basename(cf), cf, sections


def _container_of(path):
    """The folder a report or media file belongs to, forward-slashed."""
    return os.path.dirname(_clean_path(path).replace('\\', '/'))


def _media_lookup(files_found):
    """(container, basename) -> raw files_found path for every file under a
    linked_media/ folder, where the container is the folder holding that
    linked_media/. Keying on the bare basename alone would let two returns (or
    two reports each carrying their own media folder) collide on a shared
    name, and the second would silently overwrite the first -- joining one
    report's record to another report's bytes. The container keeps them
    apart."""
    lookup = {}
    marker = '/linked_media/'
    for raw in files_found:
        cf = _clean_path(raw).replace('\\', '/')
        idx = cf.find(marker)
        if idx != -1:
            lookup[(cf[:idx], os.path.basename(cf))] = raw
    return lookup


def _media_cell(linked_value, media_files, container):
    """Resolve a 'linked_media/<file>' reference from the report against the
    files actually present in the return, preferring the media folder that
    belongs to the report being parsed. Returns (media_ref_or_'', status)."""
    if not linked_value:
        return '', ''
    name = linked_value.strip().replace('\\', '/').split('/')[-1]
    raw = media_files.get((container, name))
    note = ''
    if raw is None:
        # Not beside this report. A single match elsewhere in the return is
        # still a single candidate, so link it and say where it came from;
        # several candidates are ambiguous and are never guessed between.
        elsewhere = [key for key in media_files if key[1] == name]
        if len(elsewhere) == 1:
            raw = media_files[elsewhere[0]]
            note = (' (resolved from a linked_media folder outside this '
                    'report folder)')
        elif len(elsewhere) > 1:
            return '', (f'{name} is present in {len(elsewhere)} different '
                        f'linked_media folders -- ambiguous, not linked; '
                        f'review manually')
    if raw:
        ref = check_in_media(raw, name) or ''
        if ref:
            return ref, 'linked' + note
        return '', 'file present but media registration failed — review'
    return '', (f'referenced as {linked_value.strip()} — file not present in '
                f'linked_media (removed or withheld)')


def _rows(pairs, start_label):
    """Group an ordered (label, value) list into row dicts, starting a new row
    at each occurrence of start_label. Values sharing a label within one row
    (e.g. repeated 'Seen' timestamps) are newline-joined. Returns list of
    dicts label -> joined value."""
    rows = []
    cur = None
    for label, val in pairs:
        if label == start_label:
            if cur is not None:
                rows.append(cur)
            cur = {}
        if cur is None:
            continue  # preamble before the first row
        cur.setdefault(label, []).append(val)
    if cur is not None:
        rows.append(cur)
    return [{k: '\n'.join(v for v in vals if v != '') for k, vals in row.items()}
            for row in rows]


def _no_records(pairs):
    """True when a section only reports 'No responsive records'."""
    vals = [v for _, v in pairs if v]
    return (not vals) or all(v.strip().lower().startswith('no responsive record')
                             for v in vals)


# ---------------------------------------------------------------------------
# Artifact functions
# ---------------------------------------------------------------------------

# Singleton profile/report sections shown as key/value in Account Information.
_ACCOUNT_SECTIONS = (
    'request_parameters', 'name', 'alternate_name', 'name_changes', 'emails',
    'email_changes', 'phone_numbers', 'removed_phone_numbers', 'vanity',
    'vanity_changes', 'registration_date', 'registration_ip',
    'account_end_date', 'account_status_history', 'gender', 'date_of_birth',
    'address', 'current_city', 'hometown', 'locale', 'spoken_languages',
    'website', 'bio', 'about_me', 'profile_uri', 'screen_names',
)


def _kv_rows(sec_title, pairs, basename, media_files, container, data_list):
    """Emit Section/Field/Value rows; values referencing linked_media get the
    file rendered in the Media column (with a status when it is absent)."""
    for label, val in pairs:
        if not val:
            continue
        media_ref, status = ('', '')
        if 'linked_media/' in val:
            media_ref, status = _media_cell(val, media_files, container)
        data_list.append((sec_title, label or sec_title, val,
                          media_ref, status, basename))


@artifact_processor
def meta_account_info(context):
    files_found = context.get_files_found()
    data_headers = ('Section', 'Field', 'Value', ('Media', 'media'),
                    'Link Status', 'Source File')
    data_list = []
    source = ''
    media_files = _media_lookup(files_found)
    for basename, cf, sections in _iter_reports(files_found):
        source = cf
        for sec_id in _ACCOUNT_SECTIONS:
            pairs = sections.get(sec_id)
            if not pairs or _no_records(pairs):
                continue
            _kv_rows(sec_id.replace('_', ' ').title(), pairs, basename,
                     media_files, _container_of(cf), data_list)
    return data_headers, data_list, (source if data_list else '')


def _ncmec_row(tip, row, basename, media_files, container):
    """Build one NCMEC output row. Module level rather than a closure inside the
    report loop so it cannot capture a loop variable (pylint W0640)."""
    media_ref, status = _media_cell(row.get('Linked Media File:', ''),
                                    media_files, container)
    return (
        tip.get('CyberTip ID', ''), _ts(tip.get('Time', '')),
        tip.get('Responsible Id', ''),
        row.get('Text and/or Media ID', ''),
        _ts(row.get('Upload Time', '')), row.get('Upload Ip', ''),
        row.get('User Generated Filename', ''),
        row.get('NCMEC File ID', ''), row.get('PhotoDNA Hash', ''),
        row.get('Human Reviewed', ''), row.get('Caption', ''),
        row.get('Sharepoint', ''), row.get('Recipients', ''),
        row.get('Industry CSAM Classification', ''),
        row.get('NCMEC Defined Product Annotations', ''),
        row.get('Reported Text', ''),
        media_ref, status, basename,
    )


@artifact_processor
def meta_ncmec_cybertips(context):
    """One row per Text/Media ID within each NCMEC CyberTip. The CyberTip-level
    fields (CyberTip ID, report time, responsible account) are repeated on each
    of its media rows."""
    files_found = context.get_files_found()
    data_headers = (
        'CyberTip ID', ('CyberTip Time (UTC)', 'datetime'), 'Responsible ID',
        'Text / Media ID', ('Upload Time (UTC)', 'datetime'), 'Upload IP',
        'User Generated Filename', 'NCMEC File ID', 'PhotoDNA Hash',
        'Human Reviewed', 'Caption', 'Sharepoint', 'Recipients',
        'Industry CSAM Classification', 'NCMEC Defined Product Annotations',
        'Reported Text', ('Media', 'media'), 'Link Status', 'Source File'
    )
    tip_fields = {'CyberTip ID', 'Time', 'Responsible Id'}
    data_list = []
    source = ''
    media_files = _media_lookup(files_found)

    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('ncmec_reports')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        container = _container_of(cf)
        tip = {}
        row = {}
        open_row = False

        for label, val in pairs:
            if label in tip_fields:
                if label == 'CyberTip ID':
                    if open_row:
                        data_list.append(
                            _ncmec_row(tip, row, basename, media_files, container))
                    row, open_row = {}, False
                    tip = {}
                tip[label] = val
            elif label == 'Text and/or Media ID':
                if open_row:
                    data_list.append(
                        _ncmec_row(tip, row, basename, media_files, container))
                row, open_row = {label: val}, True
            elif open_row and label:
                # keep the first occurrence; later values on the same label are
                # appended rather than overwriting it
                existing = row.get(label, '')
                if existing and val:
                    row[label] = existing + '\n' + val
                elif not existing:
                    row[label] = val
        if open_row:
            data_list.append(_ncmec_row(tip, row, basename, media_files, container))

    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_ip_addresses(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Time (UTC)', 'datetime'), 'IP Address (:port)', 'Action',
        'Agent String', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('ip_addresses')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'IP Address'):
            data_list.append((
                _ts(row.get('Time', '')), row.get('IP Address', ''),
                row.get('Action', ''), row.get('Agent String', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


def _post_rows(post, atts, basename, media_files, container):
    """Rows for one group post: one per attachment so each media file renders on
    its own row, one bare row when the post has no attachment. Module level
    rather than a closure inside the report loop (pylint W0640)."""
    rows = []
    for att in (atts or [{}]):
        media_ref, status = _media_cell(att.get('Linked Media File:', ''),
                                        media_files, container)
        rows.append((
            _ts(post.get('Post Date', '')), post.get('Id', ''),
            post.get('Post Author', ''), post.get('Post', ''),
            att.get('Type', ''), _ts(att.get('Time', '')),
            media_ref, status, att.get('URL', ''), basename,
        ))
    return rows


@artifact_processor
def meta_group_messages(context):
    """Group posts; one output row per attachment so each media file renders on
    its own row (posts without attachments get a single row)."""
    files_found = context.get_files_found()
    data_headers = (
        ('Post Date (UTC)', 'datetime'), 'Post ID', 'Post Author', 'Post',
        'Attachment Type', ('Attachment Time (UTC)', 'datetime'),
        ('Media', 'media'), 'Link Status', 'Attachment URL', 'Source File'
    )
    post_fields = ('Id', 'Post Author', 'Post Date', 'Post')
    att_fields = ('Description', 'Time', 'Type', 'URL', 'Linked Media File:')
    data_list = []
    source = ''
    media_files = _media_lookup(files_found)

    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('group_messages')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        container = _container_of(cf)

        post, atts = None, []
        for label, val in pairs:
            if label == 'Id':
                if post is not None:
                    data_list.extend(
                        _post_rows(post, atts, basename, media_files, container))
                post, atts = {label: val}, []
            elif post is None:
                continue
            elif label in post_fields:
                post[label] = val
            elif label in att_fields:
                # 'Description' opens a new attachment; other attachment
                # fields extend the current one (opening one if needed).
                if label == 'Description' or not atts:
                    atts.append({})
                atts[-1][label] = val
        if post is not None:
            data_list.extend(
                _post_rows(post, atts, basename, media_files, container))

    return data_headers, data_list, (source if data_list else '')


def _media_table(files_found, section_id, id_label='Id'):
    """Shared row builder for the videos/photos sections."""
    data_list = []
    source = ''
    media_files = _media_lookup(files_found)
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get(section_id)
        if not pairs or _no_records(pairs):
            continue
        source = cf
        rows = _rows(pairs, 'Author') or _rows(pairs, 'Id')
        if not rows:
            logfunc(f'Meta Business Record: {section_id} section in {basename} '
                    f'has content but no recognizable rows — inspect manually.')
            continue
        container = _container_of(cf)
        for row in rows:
            media_ref, status = _media_cell(row.get('Linked Media File:', ''),
                                            media_files, container)
            data_list.append((
                _ts(row.get('Uploaded', '')), row.get(id_label, ''),
                row.get('Author', ''), row.get('Title', ''),
                row.get('Description', ''), row.get('Link', ''),
                row.get('Upload Ip', ''), row.get('Privacy Setting', ''),
                row.get('Likes Count', ''), row.get('Reactions Count', ''),
                row.get('Comments Count', ''), row.get('Share Count', ''),
                media_ref, status, basename,
            ))
    return data_list, source


_MEDIA_HEADERS = (
    ('Uploaded (UTC)', 'datetime'), 'ID', 'Author', 'Title', 'Description',
    'Link', 'Upload IP', 'Privacy Setting', 'Likes', 'Reactions', 'Comments',
    'Shares', ('Media', 'media'), 'Link Status', 'Source File'
)


@artifact_processor
def meta_videos(context):
    files_found = context.get_files_found()
    data_list, source = _media_table(files_found, 'videos')
    return _MEDIA_HEADERS, data_list, (source if data_list else '')


@artifact_processor
def meta_photos(context):
    files_found = context.get_files_found()
    data_list, source = _media_table(files_found, 'photos')
    return _MEDIA_HEADERS, data_list, (source if data_list else '')


@artifact_processor
def meta_devices(context):
    files_found = context.get_files_found()
    data_headers = (
        'OS Type', 'OS Version', 'Device Type', 'Active', 'Is Tablet',
        'Family Device ID', ('First Seen (UTC)', 'datetime'),
        ('Last Seen (UTC)', 'datetime'), 'Blocked Status', 'User Agent',
        'Family ID History', 'App Scoped Device IDs', 'App Last Seen',
        'Associated Users', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('devices_info')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Os Type'):
            data_list.append((
                row.get('Os Type', ''), row.get('Os Version', ''),
                row.get('Device Type', ''), row.get('Active', ''),
                row.get('Is Tablet', ''), row.get('Family Device Id', ''),
                _ts(row.get('Family Device First Seen', '')),
                _ts(row.get('Family Device Last Seen', '')),
                row.get('Blocked Status', ''), row.get('User Agent', ''),
                row.get('Value', ''), row.get('App Id', ''),
                row.get('Last Seen', ''), row.get('Associated Users', ''),
                basename,
            ))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_recognized_devices(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Date Created (UTC)', 'datetime'), 'Name', 'Device and Browser',
        'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('recognized_devices')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Date Created'):
            data_list.append((
                _ts(row.get('Date Created', '')), row.get('Name', ''),
                row.get('Device and Browser', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_cookies(context):
    files_found = context.get_files_found()
    data_headers = (
        'Cookie', ('First Seen (UTC)', 'datetime'), 'Seen Count',
        'Users', 'Seen Times', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('machines')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Cookie'):
            data_list.append((
                row.get('Cookie', ''), _ts(row.get('First Seen', '')),
                row.get('Seen Count', ''), row.get('User', ''),
                row.get('Seen', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


_FRIEND_LINE = re.compile(r'^(.*?)\s*\((?:Facebook:\s*)?(\d+)\)\s*$')


@artifact_processor
def meta_friends(context):
    files_found = context.get_files_found()
    data_headers = ('Friend Name', 'Facebook ID', 'Source File')
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('friends')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for _, val in pairs:
            for line in val.split('\n'):
                line = line.strip()
                if not line:
                    continue
                m = _FRIEND_LINE.match(line)
                if m:
                    data_list.append((m.group(1), m.group(2), basename))
                else:
                    data_list.append((line, '', basename))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_friend_requests(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Time (UTC)', 'datetime'), 'Sender', 'Recipient', 'Accepted',
        'Rejected', 'Hidden', 'Marked As Spam', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('friend_requests')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Sender'):
            data_list.append((
                _ts(row.get('Time', '')), row.get('Sender', ''),
                row.get('Recipient', ''), row.get('Accepted', ''),
                row.get('Rejected', ''), row.get('Hidden', ''),
                row.get('Marked As Spam', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_groups(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Join Date (UTC)', 'datetime'), 'Group Name', 'Group ID', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('groups')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Name'):
            data_list.append((
                _ts(row.get('Join Date', '')), row.get('Name', ''),
                row.get('Id', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_support_correspondence(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Time Created (UTC)', 'datetime'), 'Ticket ID', 'Ticket Subject',
        'Message From', 'Message To', 'Message Subject', 'Message Time',
        'Message Body', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('support_correspondence')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Ticket ID'):
            data_list.append((
                _ts(row.get('Time Created', '')), row.get('Ticket ID', ''),
                row.get('Ticket Subject', ''), row.get('From', ''),
                row.get('To', ''), row.get('Subject', ''),
                row.get('Time', ''), row.get('Body', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_payment_info(context):
    files_found = context.get_files_found()
    data_headers = (
        'Type', 'Card Type', 'BIN', 'Last 4', 'Payment Account ID',
        'Payment Credential ID', 'Name', 'Address', 'Country', 'Details',
        'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('credit_cards')
        if pairs and not _no_records(pairs):
            source = cf
            for row in _rows(pairs, 'Card Type'):
                name = ' '.join(x for x in (row.get('First', ''),
                                            row.get('Middle', ''),
                                            row.get('Last', '')) if x)
                addr = ', '.join(x for x in (row.get('Street', ''),
                                             row.get('Street2', ''),
                                             row.get('City', ''),
                                             row.get('State', ''),
                                             row.get('Zip', '')) if x)
                data_list.append((
                    'Credit Card', row.get('Card Type', ''), row.get('BIN', ''),
                    row.get('Last 4', ''), row.get('Payment Account ID', ''),
                    row.get('Payment Credential ID', ''), name, addr,
                    row.get('Country', ''), '', basename,
                ))
        for sec_id, type_name in (('paypal_accounts', 'PayPal'),
                                  ('direct_debit', 'Direct Debit'),
                                  ('payment_accounts', 'Payment Account')):
            pairs = sections.get(sec_id)
            if not pairs or _no_records(pairs):
                continue
            source = cf
            details = '\n'.join(f'{l}: {v}' if l else v
                                for l, v in pairs if v)
            data_list.append((type_name, '', '', '', '', '', '', '', '',
                              details, basename))
    return data_headers, data_list, (source if data_list else '')


@artifact_processor
def meta_linked_accounts(context):
    files_found = context.get_files_found()
    data_headers = (
        ('Time (UTC)', 'datetime'), 'Service', 'Identifier', 'Source File'
    )
    data_list = []
    source = ''
    for basename, cf, sections in _iter_reports(files_found):
        pairs = sections.get('linked_accounts')
        if not pairs or _no_records(pairs):
            continue
        source = cf
        for row in _rows(pairs, 'Service'):
            data_list.append((
                _ts(row.get('Time', '')), row.get('Service', ''),
                row.get('Identifier', ''), basename,
            ))
    return data_headers, data_list, (source if data_list else '')


# Sections rendered by the dedicated artifacts above.
_COVERED_SECTIONS = set(_ACCOUNT_SECTIONS) | {
    'ncmec_reports', 'ip_addresses', 'group_messages', 'videos', 'photos',
    'devices_info', 'recognized_devices', 'machines', 'friends',
    'friend_requests', 'groups', 'support_correspondence', 'credit_cards',
    'paypal_accounts', 'direct_debit', 'payment_accounts', 'linked_accounts',
}


@artifact_processor
def meta_other_sections(context):
    """Every report section without a dedicated artifact, dumped as
    Section/Field/Value rows in document order so nothing in the return is
    silently dropped (e.g. unified_messages, wallposts, checkins when present)."""
    files_found = context.get_files_found()
    data_headers = ('Section', 'Field', 'Value', ('Media', 'media'),
                    'Link Status', 'Source File')
    data_list = []
    source = ''
    media_files = _media_lookup(files_found)
    for basename, cf, sections in _iter_reports(files_found):
        source = cf
        for sec_id, pairs in sections.items():
            if sec_id in _COVERED_SECTIONS:
                continue
            if not pairs or _no_records(pairs):
                continue
            _kv_rows(sec_id.replace('_', ' ').title(), pairs, basename,
                     media_files, _container_of(cf), data_list)
    return data_headers, data_list, (source if data_list else '')
