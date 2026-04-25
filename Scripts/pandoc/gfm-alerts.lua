-- gfm-alerts.lua
-- Style GitHub-flavored markdown alerts in PDF output.
--
-- Pandoc's GFM reader converts `> [!KIND]` blockquotes into a Div with class
-- `note`/`tip`/`important`/`warning`/`caution`, plus an inner Div of class
-- `title` carrying the label. For LaTeX output we wrap the body in a
-- tcolorbox-based environment defined in Scripts/pandoc/header.tex; for any
-- other format we fall back to a bold-labelled blockquote so the alert still
-- reads sensibly.

local KINDS = {
  note      = { latex = "appnalertnote",      label = "Note"      },
  tip       = { latex = "appnalerttip",       label = "Tip"       },
  important = { latex = "appnalertimportant", label = "Important" },
  warning   = { latex = "appnalertwarning",   label = "Warning"   },
  caution   = { latex = "appnalertcaution",   label = "Caution"   },
}

local function find_kind(classes)
  for _, c in ipairs(classes) do
    if KINDS[c:lower()] then return KINDS[c:lower()] end
  end
  return nil
end

function Div(el)
  local kind = find_kind(el.classes)
  if not kind then return nil end

  -- Strip the inner ``title`` Div pandoc inserts for the alert label; our
  -- environments render their own header.
  local body = {}
  for _, child in ipairs(el.content) do
    local is_title = child.t == "Div"
      and child.classes
      and #child.classes > 0
      and child.classes[1] == "title"
    if not is_title then
      table.insert(body, child)
    end
  end

  if FORMAT:match("latex") then
    local out = { pandoc.RawBlock("latex", "\\begin{" .. kind.latex .. "}") }
    for _, b in ipairs(body) do table.insert(out, b) end
    table.insert(out, pandoc.RawBlock("latex", "\\end{" .. kind.latex .. "}"))
    return out
  else
    local label = pandoc.Strong({ pandoc.Str(kind.label .. ":") })
    if body[1] and (body[1].t == "Para" or body[1].t == "Plain") then
      table.insert(body[1].content, 1, pandoc.Space())
      table.insert(body[1].content, 1, label)
    else
      table.insert(body, 1, pandoc.Para({ label }))
    end
    return pandoc.BlockQuote(body)
  end
end
