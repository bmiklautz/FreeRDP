
#include <freerdp/gdi/gdi.h>

#include <freerdp/gdi/dc.h>
#include <freerdp/gdi/pen.h>
#include <freerdp/gdi/shape.h>
#include <freerdp/gdi/region.h>
#include <freerdp/gdi/bitmap.h>

#include <winpr/crt.h>
#include <winpr/print.h>

#include "line.h"
#include "brush.h"
#include "clipping.h"
#include "helpers.h"

/* Ellipse() Test Data */

static const BYTE ellipse_case_1[256] = { "\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF" };

static const BYTE ellipse_case_2[256] = { "\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF" };

static const BYTE ellipse_case_3[256] = { "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
	                                      "\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF"
	                                      "\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	                                      "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" };

int TestGdiEllipse(int argc, char* argv[])
{
	int rc = -1;
	UINT32 i, j;
	const UINT32 RawFormat = PIXEL_FORMAT_RGB8;
	const UINT32 colorFormats[] = {
		PIXEL_FORMAT_RGB15,  PIXEL_FORMAT_ARGB15, PIXEL_FORMAT_RGB16,  PIXEL_FORMAT_RGB24,
		PIXEL_FORMAT_ARGB32, PIXEL_FORMAT_XRGB32, PIXEL_FORMAT_RGBA32, PIXEL_FORMAT_RGBX32,
		PIXEL_FORMAT_BGR15,  PIXEL_FORMAT_ABGR15, PIXEL_FORMAT_BGR16,  PIXEL_FORMAT_BGR24,
		PIXEL_FORMAT_ABGR32, PIXEL_FORMAT_XBGR32, PIXEL_FORMAT_BGRA32, PIXEL_FORMAT_BGRX32
	};
	const UINT32 number_formats = sizeof(colorFormats) / sizeof(colorFormats[0]);
	gdiPalette g;

	for (i = 0; i < number_formats; i++)
	{
		HGDI_DC hdc = NULL;
		HGDI_PEN pen = NULL;
		HGDI_BITMAP hBmp = NULL;
		HGDI_BITMAP hBmp_Ellipse_1 = NULL;
		HGDI_BITMAP hBmp_Ellipse_2 = NULL;
		HGDI_BITMAP hBmp_Ellipse_3 = NULL;
		const UINT32 format = colorFormats[i];
		gdiPalette* hPalette = &g;
		g.format = format;

		for (j = 0; j < 256; j++)
			g.palette[i] = FreeRDPGetColor(format, j, j, j, 0xFF);

		rc = -1;

		if (!(hdc = gdi_GetDC()))
		{
			printf("failed to get gdi device context\n");
			goto fail;
		}

		hdc->format = format;
		gdi_SetNullClipRgn(hdc);

		if (!(pen = gdi_CreatePen(1, 1, 0, format, hPalette)))
		{
			printf("gdi_CreatePen failed\n");
			goto fail;
		}

		gdi_SelectObject(hdc, (HGDIOBJECT) pen);
		hBmp = gdi_CreateCompatibleBitmap(hdc, 16, 16);
		gdi_SelectObject(hdc, (HGDIOBJECT) hBmp);
		hBmp_Ellipse_1 = test_convert_to_bitmap(ellipse_case_1, RawFormat, 0, 0, 0, format, 0, 0, 0, 16, 16, hPalette);

		if (!hBmp_Ellipse_1)
			goto fail;

		hBmp_Ellipse_2 = test_convert_to_bitmap(ellipse_case_2, RawFormat, 0, 0, 0, format, 0, 0, 0, 16, 16, hPalette);

		if (!hBmp_Ellipse_2)
			goto fail;

		hBmp_Ellipse_3 = test_convert_to_bitmap(ellipse_case_3, RawFormat, 0, 0, 0, format, 0, 0, 0, 16, 16, hPalette);

		if (!hBmp_Ellipse_3)
			goto fail;

		/* Test Case 1: (0,0) -> (16, 16) */
		if (!gdi_BitBlt(hdc, 0, 0, 16, 16, hdc, 0, 0, GDI_WHITENESS, hPalette))
		{
			printf("gdi_BitBlt failed (line #%u)\n", __LINE__);
			goto fail;
		}

		if (!gdi_Ellipse(hdc, 0, 0, 15, 15))
			goto fail;

		rc = 0;
	fail:
		gdi_DeleteObject((HGDIOBJECT) hBmp_Ellipse_1);
		gdi_DeleteObject((HGDIOBJECT) hBmp_Ellipse_2);
		gdi_DeleteObject((HGDIOBJECT) hBmp_Ellipse_3);
		gdi_DeleteObject((HGDIOBJECT) hBmp);
		gdi_DeleteObject((HGDIOBJECT) pen);
		gdi_DeleteDC(hdc);

		if (rc != 0)
			break;
	}

	return rc;
}
