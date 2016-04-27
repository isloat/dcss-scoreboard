"""Utility functions for website generation."""

import datetime

import dateutil.parser

from . import model
from . import modelutils
from . import constants as const

DATE_FORMAT = '%-d %B %Y'


def prettyint(value):
    """Jinja filter to prettify ints.

    eg, 1234567 to '1,234,567'.
    """
    return "{0:,}".format(value)


def prettydur(duration, hours=False):
    """Jinja filter to convert seconds to a pretty duration "HH:MM:SS".

    Parameters:
        hours (bool) Convert to only hours (with a minimum of 1 -- for player
            'hours played' metric).

    Examples:
        prettydur(170) => '0:2:50'
        prettydur(0, hours=True) => '1'
        prettydur(86400, hours=True) => '24'
    """
    if type(duration) != int:
        duration = int(duration)
    delta = datetime.timedelta(seconds=duration)
    if hours:
        dur = delta.total_seconds()/3600
        return str(int(dur)) if dur > 1 else '1'
    else:
        return str(delta)


def prettycounter(counter):
    """Jinja filter to convert a counter dict to pretty text.

    Sorts by lexical order of keys.

    eg, {'c':1, 'b': 3, 'a': 2} to 'a (2), c (1), b (3)'.
    """
    return ", ".join("{open}{k} ({v}){close}".format(
        k=k,
        v=v,
        open="" if v > 0 else '<span class="text-muted">',
        close="" if v > 0 else '</span>')
                     for k, v in sorted(counter.items(),
                                        key=lambda i: i[0]))


def prettycrawldate(d):
    """Jinja filter to convert crawl date string to pretty text."""
    return modelutils.crawl_date_to_datetime(d).strftime(DATE_FORMAT)


def prettydate(d):
    """Jinja filter to convert datetime object to pretty text."""
    return d.strftime(DATE_FORMAT)


def gamestotable(games,
                 *,
                 prefix_col=None,
                 prefix_col_title=None,
                 show_player=False,
                 winning_games=False,
                 sort_col=None):
    """Jinja filter to convert a list of games into a standard table.

    Parameters:
        prefix_col (str): Add an extra column at the start with data from
                          game.raw_data.
                          The table will also be sorted by this column.
        prefix_col_title (str): Title for the prefix_col column
        sort_col (str): Sort the table by this column from game.raw_data.
        show_player (bool): Show the player name column
        winning_games (bool): The table has only winning games, so don't show
                              place or end columns, and do show runes.

    Returns: (string) '<tr>contents</tr>'.
    """
    def format_trow(game):
        """Convert a game to a table row."""
        return trow.format(
            win='table-success' if game.ktyp == 'winning' else '',
            prefix_col='' if not prefix_col else "<td>%s</td>" %
                game.raw_data.get(prefix_col),
            player_row='' if not show_player else
            "<td><a href='{base}/players/{name}.html'>{name}</a></td>".format(
                base=const.WEBSITE_URLBASE,
                name=game.name),
            score=prettyint(game.sc),
            character=game.char,
            god=game.god,
            place="" if winning_games else "<td>%s</td>" % game.place,
            end="" if winning_games else "<td>%s</td>" % game.raw_data.get('tmsg'),
            turns=prettyint(game.turn),
            duration=prettydur(game.dur),
            date=prettydate(game.end),
            version=game.v,
            morgue=morgue_link(game))

    t = """<table class="{classes}">
          <thead>
            <tr>
            {thead}
            </tr>
          </thead>
          <tbody>
            {tbody}
          </tbody>
        </table>"""

    classes = const.TABLE_CLASSES

    thead = """{prefix}
              {player}
              <th>Score</th>
              <th>Character</th>
              <th>God</th>
              {place}
              {end}
              <th>Turns</th>
              <th>Duration</th>
              <th>Date</th>
              <th>Version</th>
              <th>Morgue File</th>""".format(
        prefix='' if not prefix_col else '<th>%s</th>' % prefix_col_title,
        player='' if not show_player else '<th>Player</th>',
        place='' if winning_games else '<th>Place</th>',
        end='' if winning_games else '<th>End</th>')

    trow = """<tr>
      {prefix_col}
      {player_row}
      <td>{score}</td>
      <td>{character}</td>
      <td>{god}</td>
      {place}
      {end}
      <td>{turns}</td>
      <td>{duration}</td>
      <td>{date}</td>
      <td>{version}</td>
      <td>{morgue}</td>
    </tr>"""

    if sort_col:
        games = sorted(games, key=lambda g: g['raw_data'][sort_col])
    elif prefix_col:
        games = sorted(games, key=lambda g: g['raw_data'][prefix_col])

    return t.format(classes=classes,
                    thead=thead,
                    tbody="\n".join(format_trow(game) for game in games))


def streaktotablerow(streak):
    """Jinja filter to convert a streak to a table row."""
    return """<tr>
      <td>{wins}</td>
      <td><a href="players/{player}.html">{player}<a></td>
      <td>{games}</td>
      <td>{start}</td>
      <td>{end}</td>
      <td>{versions}</td>
    </tr>""".format(
        wins=len(streak['wins']),
        player=streak['player'],
        games=', '.join(morgue_link(model.game(g), model.game(g).char) for g in streak['wins']),
        start=prettydate(dateutil.parser.parse(streak['start'])),
        end=prettydate(dateutil.parser.parse(streak['end'])),
        versions=', '.join(sorted(set(model.game(g).v for g in streak[
            'wins']))))


def longeststreaktotablerow(streak):
    """Jinja filter to convert a streak to a table row."""
    return """<tr>
      <td>{wins}</td>
      <td><a href="players/{player}.html">{player}<a></td>
      <td>{games}</td>
      <td>{start}</td>
      <td>{end}</td>
      <td>{versions}</td>
      <td>{streak_breaker}</td>
    </tr>""".format(
        wins=len(streak['wins']),
        player=streak['player'],
        games=', '.join(morgue_link(model.game(g), model.game(g).char) for g in streak['wins']),
        start=prettydate(dateutil.parser.parse(streak['start'])),
        end='' if 'streak_breaker' not in streak else prettydate(
            dateutil.parser.parse(streak['end'])),
        versions=', '.join(sorted(set(model.game(g).v for g in streak[
            'wins']))),
        streak_breaker=morgue_link(model.game(streak[
            'streak_breaker']), model.game(streak[
            'streak_breaker']).char) if 'streak_breaker' in streak else '')


def morgue_link(game, text="Morgue"):
    """Returns a hyperlink to a morgue file.

    Game can be either a gid string or a game object.
    """
    if type(game) is str:
        # Treat as gid
        game = model.game(game)
    result = "<a href='" + modelutils.morgue_url(game) + "'>" + text + "</a>"
    return result
