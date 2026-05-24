-- table-widths.lua — assign relative column widths to every Table so the
-- LaTeX writer emits `p{...}` paragraph columns (which wrap) instead of
-- the default `l` columns (which run off the page).
--
-- Width per column = max plain-text length of the header + body cells in
-- that column, normalised so the row sums to 1.0. A small minimum share
-- per column prevents very narrow columns from collapsing to nothing.

local MIN_SHARE = 0.06   -- floor (~6% of \linewidth) per column
local MIN_LEN   = 4      -- treat shorter cells as this many chars
local SUM_CAP   = 1.0    -- pandoc expects widths summing to <= 1.0

local function cell_text_len(cell)
  -- pandoc.utils.stringify gives a plain-text rendering we can measure.
  local s = pandoc.utils.stringify(cell.contents or cell)
  -- Approximate visual width: code spans and short tokens shouldn't
  -- dominate. Use raw character count, with a small floor.
  local n = #s
  if n < MIN_LEN then n = MIN_LEN end
  return n
end

local function row_cell_lengths(row, lens)
  for i, cell in ipairs(row.cells) do
    local n = cell_text_len(cell)
    if not lens[i] or n > lens[i] then
      lens[i] = n
    end
  end
end

function Table(tbl)
  local ncols = #tbl.colspecs
  if ncols == 0 then return nil end

  -- Gather max content length per column across header + body rows.
  local lens = {}
  for _ = 1, ncols do lens[#lens + 1] = MIN_LEN end

  for _, row in ipairs(tbl.head.rows or {}) do
    row_cell_lengths(row, lens)
  end
  for _, body in ipairs(tbl.bodies or {}) do
    for _, row in ipairs(body.body or {}) do
      row_cell_lengths(row, lens)
    end
  end

  -- Apply the per-column floor, then normalise so widths sum to SUM_CAP.
  local total = 0
  for i = 1, ncols do total = total + lens[i] end
  if total <= 0 then return nil end

  local shares = {}
  local remaining = SUM_CAP
  local n_floored = 0
  for i = 1, ncols do
    local share = (lens[i] / total) * SUM_CAP
    if share < MIN_SHARE then
      share = MIN_SHARE
      n_floored = n_floored + 1
    end
    shares[i] = share
    remaining = remaining - share
  end

  -- If flooring pushed the sum over SUM_CAP, rescale non-floored columns
  -- to absorb the deficit.
  if remaining < 0 then
    local non_floored_total = 0
    for i = 1, ncols do
      if shares[i] > MIN_SHARE then
        non_floored_total = non_floored_total + shares[i]
      end
    end
    if non_floored_total > 0 then
      local scale = (non_floored_total + remaining) / non_floored_total
      if scale < 0 then scale = 0 end
      for i = 1, ncols do
        if shares[i] > MIN_SHARE then
          shares[i] = shares[i] * scale
        end
      end
    end
  end

  for i, spec in ipairs(tbl.colspecs) do
    tbl.colspecs[i] = { spec[1], shares[i] }
  end
  return tbl
end
