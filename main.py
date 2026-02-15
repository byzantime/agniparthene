#!/usr/bin/env python3
"""Build script for Agni Parthene website."""

from pathlib import Path
from hardboiled import SiteBuilder, current_year
from config import SITE_CONFIG


def build():
    """Build the static site."""
    builder = SiteBuilder(
        template_dir="src/templates",
        static_dir="src/static",
        build_dir="build",
        base_path=Path.cwd(),
    )

    # Ensure build directories exist
    builder.ensure_build_dirs(subdirs=["static/css"])

    # Add global template variables
    builder.add_global("site", SITE_CONFIG)
    builder.add_global("current_year", current_year())

    # Hymn content - all 24 stanzas with refrains
    # Each strophe uses 3 tunes (A, B, Γ), each sung twice
    hymn_verses = [
        # Strophe 1
        {
            "greek": "Ἁγνὴ Παρθένε Δέσποινα, ἄχραντε Θεοτόκε,",
            "english": "O pure and virgin Lady, O spotless Theotokos,",
            "tune": "A",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Παρθένε μήτηρ ἄνασσα, πανένδροσέ τε πόκε,",
            "english": "O Virgin Queen and Mother, O dewy Fleece most sacred,",
            "tune": "A",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Ὑψηλοτέρα οὐρανῶν, ἀκτίνων λαμπροτέρα,",
            "english": "O height transcending heaven above, O beam of light most radiant,",
            "tune": "B",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Χαρὰ παρθενικῶν χορῶν, ἀγγέλων ὑπερτέρα,",
            "english": "O joy of chaste and virgin maids, surpassing all the angels,",
            "tune": "B",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Ἐκλαμπροτέρα οὐρανῶν, φωτὸς καθαρωτέρα,",
            "english": "O brilliant light of heaven above, most clear and most radiant,",
            "tune": "Γ",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        {
            "greek": "Τῶν οὐρανίων στρατιῶν, πασῶν ἁγιωτέρα,",
            "english": "Commanding Chief of heavenly hosts, O holiest of holies,",
            "tune": "Γ",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        # Strophe 2
        {
            "greek": "Μαρία ἀειπάρθενε, κόσμου παντὸς Κυρία,",
            "english": "O ever virgin Mary, O Mistress of creation,",
            "tune": "A",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Ἄχραντε νύμφη πάναγνε, Δέσποινα Παναγία,",
            "english": "O Bride all pure and spotless, O Lady all holy,",
            "tune": "A",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Μαρία νύμφη ἄνασσα, χαρᾶς ἡμῶν αἰτία,",
            "english": "O holy Mary, Bride and Queen, O cause of our rejoicing,",
            "tune": "B",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Κόρη σεμνή, Βασίλισσα, Μήτηρ ὑπεραγία,",
            "english": "O Maiden Queen honorable, O Mother most holy,",
            "tune": "B",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Τιμιωτέρα Χερουβείμ, ὑπερενδοξοτέρα,",
            "english": "More precious than the Cherubim, and more glorious than the Seraphim,",
            "tune": "Γ",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        {
            "greek": "Τῶν ἀσωμάτων Σεραφείμ, τῶν θρόνων ὑπερτέρα,",
            "english": "Surpassing Principalities, Dominions, Thrones, and Powers,",
            "tune": "Γ",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        # Strophe 3
        {
            "greek": "Χαῖρε τὸ ᾆσμα Χερουβείμ, χαῖρε ὕμνος ἀγγέλων,",
            "english": "Rejoice, song of the Cherubim; Rejoice, hymn of the Angels,",
            "tune": "A",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Χαῖρε ᾠδὴ τῶν Σεραφείμ, χαρὰ τῶν ἀρχαγγέλων,",
            "english": "Rejoice, ode of the Seraphim, and joy of the Archangels,",
            "tune": "A",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Χαῖρε εἰρήνη καὶ χαρά, λιμὴν τῆς σωτηρίας,",
            "english": "Rejoice, O peace, Rejoice, O joy, and haven of salvation,",
            "tune": "B",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Παστὰς τοῦ Λόγου ἱερά, ἄνθος τῆς ἀφθαρσίας,",
            "english": "O bridal chamber of the Word, unfading, fragrant blossom,",
            "tune": "B",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Χαῖρε Παράδεισε τρυφῆς, ζωῆς τε αἰωνίας,",
            "english": "Rejoice, delight of paradise, Rejoice, life everlasting,",
            "tune": "Γ",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        {
            "greek": "Χαῖρε τὸ ξύλον τῆς ζωῆς, πηγὴ ἀθανασίας,",
            "english": "Rejoice, O holy Tree of Life, and Fount of immortality,",
            "tune": "Γ",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        # Strophe 4
        {
            "greek": "Σὲ ἱκετεύω Δέσποινα, Σὲ νῦν ἐπικαλοῦμαι,",
            "english": "I supplicate thee, Lady, I humbly call upon thee!",
            "tune": "A",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Σὲ δυσωπῶ Παντάνασσα, Σὴν χάριν ἐξαιτοῦμαι,",
            "english": "O Queen of all, I beg thee, to grant me thy favor,",
            "tune": "A",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "A",
        },
        {
            "greek": "Κόρη σεμνὴ καὶ ἄσπιλε, Δέσποινα Παναγία,",
            "english": "O spotless and most honoured Maid, O Lady all holy,",
            "tune": "B",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Θερμῶς ἐπικαλοῦμαί Σε, ναὲ ἡγιασμένε,",
            "english": "I call upon thee fervently, thou temple most holy,",
            "tune": "B",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "B",
        },
        {
            "greek": "Ἀντιλαβοῦ μου, ῥῦσαί με, ἀπὸ τοῦ πολεμίου,",
            "english": "O thou my help, deliver me from harm and all adversity,",
            "tune": "Γ",
            "tune_start": True,
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
        {
            "greek": "Καὶ κληρονόμον δεῖξόν με, ζωῆς τῆς αἰωνίου,",
            "english": "And by thy prayers show me to be an heir of immortality,",
            "tune": "Γ",
        },
        {
            "greek": "Χαῖρε νύμφη ἀνύμφευτε.",
            "english": "Rejoice, O unwedded Bride!",
            "refrain": True,
            "tune": "Γ",
        },
    ]

    # Context for templates
    context = {
        "hymn_verses": hymn_verses,
    }

    # Render pages
    builder.render_pages(
        pages=["index.html"],
        context=context,
    )

    # Copy static assets (CSS will be built by Tailwind separately)
    builder.copy_static_assets(exclude_patterns=["*.css"])

    print("Build complete!")


if __name__ == "__main__":
    build()
